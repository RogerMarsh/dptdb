# run_test_create_databases.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

"""
import open_dpt_database
import record_tuples


def run_test_create_databases(
    default_records=200, brecppg=50, btod_factor=1, items=None
):
    """Run tests for all the database definitions in file_definitions."""
    if items is None:
        items = ()
    print(
        "enter run_test_create_databases",
        "allowing",
        default_records,
        "records",
    )
    for name, definition, records in items:
        del records
        print("enter create_database for", name)
        open_dpt_database.open_dpt_database(
            name,
            definition(
                default_records=default_records,
                brecppg=brecppg,
                btod_factor=btod_factor,
            ),
        ).close_database()
        print("leave create_database for", name)
    print("done")


if __name__ == "__main__":
    run_test_create_databases(items=record_tuples.all_record_generators)
