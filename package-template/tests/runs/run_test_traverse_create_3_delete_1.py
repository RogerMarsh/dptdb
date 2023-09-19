# run_test_create_3_delete_1.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add 3 records to database without ordered fields and delete record 0.

This causes RuntimeError 'Bit subscript out of mapped range' in the
simplest possible situation: one record with a non-zero record number
and one unordered field.

"""
import os

from dptdb import dptapi

import dpt_database
import file_definitions
import record_tuples
import add_records


def rttc3d1_one_file_one_field(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database with one file and one field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.one_file_one_field(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )
    directory = dpt_database.directory_with_bitness()
    directory = os.path.join(directory, file_definitions.ONE_FILE_ONE_FIELD)
    database = dpt_database.DPTDatabase(
        directory,
        deferred=deferred,
        filedefs=file_definitions.one_file_one_field(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    database.create()
    try:
        for file, context in database.contexts.items():
            foundset = context.FindRecords(
                dptapi.APIFindSpecification(dptapi.FD_SINGLEREC, 0)
            )
            try:
                cursor = foundset.OpenCursor()
                try:
                    cursor.GotoFirst()
                    while True:
                        if not cursor.Accessible():
                            break
                        current = cursor.AccessCurrentRecordForReadWrite()
                        current.Delete()
                        cursor.Advance(1)
                    database.database_services.Commit()
                finally:
                    foundset.CloseCursor(cursor)
                    del cursor
            finally:
                context.DestroyRecordSet(foundset)
                del foundset
            foundset = context.FindRecords()
            try:
                assert foundset.Count() == default_records - 1
                for advance in (1, -1):
                    cursor = foundset.OpenCursor()
                    ebm_count = 0
                    recnum = None
                    try:
                        if advance == 1:
                            cursor.GotoFirst()
                        else:
                            cursor.GotoLast()
                        while True:
                            if not cursor.Accessible():
                                break
                            ebm_count += 1
                            recnum = cursor.AccessCurrentRecordForRead(
                                ).RecNum()
                            cursor.Advance(advance)
                    except RuntimeError as exc:
                        print("ebm advance", advance, ebm_count)
                        print("recnum", recnum)
                        raise
                    finally:
                        foundset.CloseCursor(cursor)
                        del cursor
            finally:
                context.DestroyRecordSet(foundset)
                del foundset
    finally:
        database.close_database()


def run_test_traverse_create_3_delete_1():
    rttc3d1_one_file_one_field(default_records=3)
    print("run_test_create_3_delete_1", "done")


if __name__ == "__main__":
    run_test_traverse_create_3_delete_1()
