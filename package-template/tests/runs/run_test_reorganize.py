# run_test_reorganize.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Reorganize database defined in file_definitions module.

This is known to work in x86 environment, although best to verify the
run can work: the test is what about x64.

The database is expected to be created by a run_test_create_and_populate_*
run.

"""
import multiprocessing

import dptdb

import open_dpt_database
import file_definitions

# Need 'replace' option because unload output files are defaulted and may
# still exist from an earlier run.
# The default directory containing the old output files will be './#FASTIO'.
_UNLOAD_OPTIONS = dptdb.dptapi.FUNLOAD_DEFAULT | dptdb.dptapi.FUNLOAD_REPLACE


def _list_field_names(context):
    """List fields in context.

    Verify fields present to check against TAPEI nonexistent field
    warnings.

    """
    fieldattrcursor = context.OpenFieldAttCursor()
    try:
        fieldattrcursor.GotoFirst()
        print("list fields")
        while True:
            if not fieldattrcursor.Accessible():
                print("fields listed")
                break
            print("field", fieldattrcursor.Name(), "exists")
            fieldattrcursor.Advance(1)
    finally:
        context.CloseFieldAttCursor(fieldattrcursor)
        del fieldattrcursor


def unload():
    """Unload the database in a normal session."""
    database = open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(),
        unload=True,
    )
    try:
        for file, context in database.contexts.items():
            print("enter Unload for", file)
            context.Unload(_UNLOAD_OPTIONS)
            print("leave Unload for", file)
            _list_field_names(context)
    finally:
        database.close_database()


def load():
    """Load the database in a non-TBO session for fastload."""
    database = open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(),
        load=True,
    )
    try:
        for file, context in database.contexts.items():
            print("enter Initialize for", file)
            context.Initialize()
            print("leave Initialize for", file)
            _list_field_names(context)
            print("enter Load for", file)
            context.Load()
            print("leave Load for", file)
            _list_field_names(context)
    finally:
        database.close_database()


def reorganize():
    """Reorganize the database."""
    process = multiprocessing.Process(target=unload)
    process.start()
    process.join()
    load()

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    print("This run assumes a run_test_create_and_populate_* has been run\n")
    print("start run_test_reorganize")
    reorganize()
    print("finish run_test_reorganize")
    print("\nRemember to delete the database")
