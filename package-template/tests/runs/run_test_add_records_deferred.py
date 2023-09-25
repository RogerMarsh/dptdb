# run_test_add_records_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

THIS MODULE DOES NOT DO IT'S TASK, because:

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

and exists only because run_test_add_records.py exists.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

All field values are unique in these tests, so lists and bitmaps are not
used to implement the inverted lists of records.

65537 records, not 200000, should be enough for this test because that is
where the ChessTab import fails in the x64 environment: the first segment
is full and a new segment is used.

However 200000 is exactly two orders of magnitude greater than the default
number of records and is enough to need four segments rather than one.

The only bitmap in use is the existence bitmap: this module tests if there
is a problem creating more than one existence bitmap segment in the x64
environment.

"""
import add_records
import open_dpt_database
import record_tuples


def run_test_add_records_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None, items=None
):
    """Run tests for all the database definitions in file_definitions."""
    if items is None:
        items = ()
    print("WARNING:    This run cannot succeed.")
    print("WARNING:    The DPT stuff for first file is done but the 'leave'")
    print("WARNING:    trace message does not get printed; and the run")
    print("WARNING:    terminates without giving any failure indication.")
    print("WARNING:    (compare with similar 'run_test_add_records' job)")
    print("WARNING:    Use 'run_test_create_databases' followed")
    print("WARNING:     by 'run_test_populate_databases_deferred' instead.")
    print(
        "enter run_test_add_records_deferred",
        "adding",
        default_records,
        "records",
    )
    for name, definition, records in items:
        print("enter create_database for", name)
        open_dpt_database.create_database(
            name,
            definition,
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        )
        print("leave create_database for", name)
        print("enter add_records for", name)
        add_records.add_records(
            name,
            definition(
                default_records=default_records,
                brecppg=brecppg,
                btod_factor=btod_factor,
            ),
            records=records,
            default_records=default_records,
            modulus=modulus,
            deferred=True,
        )
        print("leave add_records for", name)
    print("done")


if __name__ == "__main__":
    run_test_add_records_deferred(items=record_tuples.all_record_generators)
