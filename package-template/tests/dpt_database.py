# dpt_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Provide class which defines, creates and deletes a database."""
import os
import shutil
    
from dptdb import dptapi

import filespec


class DPTDatabase:
    """Define database."""

    def __init__(self, directory, deferred=False, filedefs=None):
        """Create DPT definition for a database in directory from filedefs."""
        self.directory = directory
        self.deferred = deferred
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

        # Use CONSOLE rather than sysprint because SYSPRNT is not fully released
        # unless Python is restarted as a new command line command.
        # To see CONSOLE run this script by python.exe rather than pythonw.exe
        sysprint = "CONSOLE"

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.exists(self.dptsys):
            os.makedirs(self.dptsys)
            
        # Set parms for normal or single-step deferred update mode
        if self.deferred:
            pf = open(parms, 'w')
            try:
                pf.write("RCVOPT=X'00' " + os.linesep)
                pf.write("MAXBUF=200 " + os.linesep)
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
                if not disp and self.deferred:
                    raise RuntimeError(
                        "Cannot oppen non-existent file for deferred update"
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
                self.allocated.add(key)
                records_per_page = value[filespec.FILEDESC][filespec.BRECPPG]
                table_b_size = value[
                    filespec.DEFAULT_RECORDS
                ] * records_per_page
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

    def delete(self):
        """Delete DPT database services."""
        if self.database_services is None:
            return
        self.close_contexts()
        self.free()
        pycwd = os.getcwd()
        os.chdir(self.dptsys)
        self.database_services.Destroy()
        try:
            os.chdir(pycwd)
            shutil.rmtree(self.directory)
        finally:
            self.database_services = None
