# dpt_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Provide class which defines, creates and deletes a database."""
import sys
import os
import shutil
    
from dptdb import dptapi

import filespec

# See documentation for platform module.
is_64bits = sys.maxsize > 2 ** 32


def directory_with_bitness():
    """Return directory with 'bitness' of Python interpreter appended.

    Used by 'run_test_*' modules to get a default directory name.

    """
    directory = os.environ.get(
        "TEMP",
        os.environ.get("TMP",os.environ.get("HOME")),
    )
    return os.path.join(
        directory, "dptdb_test" + ("64" if is_64bits else "32"),
    )


class DPTDatabase:
    """Define database."""

    def __init__(
        self,
        directory,
        deferred=False,
        load=False,
        unload=False,
        filedefs=None,
    ):
        """Create DPT definition for a database in directory from filedefs.

        load is ignored if bool(deferred) is True.
        unload is ignored if bool(deferred) is True.
        unload is ignored if bool(load) is True.

        """
        self.directory = directory
        self.deferred = deferred
        self.load = load
        self.unload = unload
        if filedefs is None:
            filedefs = {}
        self.filespec = filespec.FileSpec(**filedefs)
        self.filespec.set_file_directory(self.directory)
        self.database_services = None
        self.allocated = set()
        self.contexts = {}
        self.dptsys = os.path.join(self.directory, 'sys')

    def create(self):
        """Create the DPT database defined in self.filespec"""
        parms = os.path.join(self.dptsys, 'parms.ini')
        msgctl = os.path.join(self.dptsys, 'msgctl.ini')
        audit = os.path.join(self.dptsys, 'audit.txt')

        # Use CONSOLE rather than sysprint because SYSPRNT is not fully
        # released unless Python is restarted as a new command line command.
        # To see CONSOLE run this script by python.exe rather than pythonw.exe
        sysprint = "CONSOLE"

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.exists(self.dptsys):
            os.makedirs(self.dptsys)
            
        # Set parms for normal, single-step deferred update, unload or
        # load mode.
        if self.deferred:
            pf = open(parms, 'w')
            try:
                pf.write("RCVOPT=X'00' " + os.linesep)
                pf.write("MAXBUF=99 " + os.linesep)
            finally:
                pf.close()
        elif self.load:
            pf = open(parms, 'w')
            try:
                pf.write("RCVOPT=X'00' " + os.linesep)
                pf.write("MAXBUF=99 " + os.linesep)
            finally:
                pf.close()
        elif self.unload:
            pf = open(parms, 'w')
            try:
                pf.write("MAXBUF=99 " + os.linesep)
            finally:
                pf.close()
        elif os.path.exists(parms):
            os.remove(parms) # assume delete will work here

        # Ensure checkpoint.ckp file and #SEQTEMP folder are created in correct
        # folder (change current working directory).
        pycwd = os.getcwd()
        os.chdir(self.dptsys)
        ds = dptapi.APIDatabaseServices(
            sysprint,
            'pyapitest',
            parms,
            msgctl,
            audit)
        try:
            os.chdir(pycwd)
        except:
            ds.Destroy()
            del ds
            raise
        self.database_services = ds
        del ds

        # Allocate, create, and open context on file, followed by initialize
        # file and create fields if it does not yet exist.
        try:
            if self.deferred:
                dsoc = self.database_services.OpenContext_DUSingle
            else:
                dsoc = self.database_services.OpenContext
            for key, value in self.filespec.items():
                disp = os.path.exists(value[filespec.FILE])
                if not disp:
                    if self.deferred:
                        raise RuntimeError(
                            "Cannot do deferred update on non-existent file"
                        )
                    if self.unload:
                        raise RuntimeError(
                            "Cannot do unload on non-existent file"
                        )
                    if self.load:
                        raise RuntimeError(
                            "Cannot do load on non-existent file"
                        )
                if disp:
                    self.database_services.Allocate(
                        value[filespec.DDNAME],
                        value[filespec.FILE],
                        dptapi.FILEDISP_OLD,
                    )
                else:
                    self.database_services.Allocate(
                        value[filespec.DDNAME],
                        value[filespec.FILE],
                        dptapi.FILEDISP_NEW,
                    )
                    records_per_page = value[
                        filespec.FILEDESC
                    ][filespec.BRECPPG]
                    table_b_size, extra = divmod(
                        value[
                            filespec.DEFAULT_RECORDS
                        ],
                        records_per_page,
                    )
                    if extra:
                        table_b_size += 1
                    self.database_services.Create(value[filespec.DDNAME],
                              table_b_size,
                              records_per_page,
                              -1,
                              -1,
                              table_b_size * value[
                                  filespec.BTOD_FACTOR
                              ] + value[filespec.BTOD_CONSTANT],
                              -1,
                              -1,
                              dptapi.FILEORG_UNORD_RRN)
                self.allocated.add(key)
                cs = dptapi.APIContextSpecification(value[filespec.DDNAME])
                oc = dsoc(cs)
                if not disp:
                    oc.Initialize()
                    for field, attributes in value[filespec.FIELDS].items():
                        fa = dptapi.APIFieldAttributes()
                        if attributes[filespec.ORD]:
                            fa.SetOrderedFlag()
                            fa.SetSplitPct(attributes[filespec.SPT])
                            if attributes[filespec.ONM]:
                                fa.SetOrdNumFlag()
                            if attributes[filespec.INV]:
                                fa.SetInvisibleFlag()
                        if attributes[filespec.FLT]:
                            fa.SetFloatFlag()
                        if attributes[filespec.UAE]:
                            fa.SetUpdateAtEndFlag()
                        oc.DefineField(field, fa)
                        del fa
                self.contexts[key] = oc
                del cs, oc
        except:
            self.delete()
            raise

    def free(self):
        """Free any allocated dpt files."""
        if self.database_services is None:
            return
        for key in self.allocated:
            self.database_services.Free(self.filespec[key][filespec.DDNAME])
        self.allocated.clear()

    def close_contexts(self):
        """Close any contexts that are open."""
        if self.database_services is None:
            return
        # for value in self.contexts.values():
        #    self.database_services.CloseContext(value)
        self.contexts.clear()
        self.database_services.CloseAllContexts(force=True)

    def __delete(self, delete_directory=False):
        """Delete DPT database services and directory if delete_directory."""
        if self.database_services is None:
            return
        self.close_contexts()
        self.free()
        pycwd = os.getcwd()
        os.chdir(self.dptsys)
        self.database_services.Destroy()
        try:
            os.chdir(pycwd)
            if delete_directory:
                shutil.rmtree(self.directory)
        finally:
            self.database_services = None

    def delete(self):
        """Delete DPT database services and database directory."""
        self.__delete(delete_directory=True)

    def close_database(self):
        """Delete DPT database services but not database directory."""
        self.__delete(delete_directory=False)

    def add_record(self, context, record=()):
        """Store record in context with fields in given order.

        The record argument must be iterable with items containing two
        elements: field and value.

        """
        template = dptapi.APIStoreRecordTemplate()
        for field, value in record:
            template.Append(field, dptapi.APIFieldValue(value))
        context.StoreRecord(template)