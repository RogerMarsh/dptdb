# run_test_add_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

All field values are unique in these tests, so lists and bitmaps are not
used to implement the inverted lists of records.

"""
import add_records
import record_tuples


def run_test_add_records(
    default_records=200, brecppg=50, btod_factor=1, modulus=None, items=None
):
    """Run tests for all the database definitions in file_definitions."""
    if items is None:
        items = ()
    print(
        "enter run_test_add_records",
        "(deferred is set False)",
        "adding",
        default_records,
        "records",
    )
    for name, definition, records in items:
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
            deferred=False,
        )
        print("leave add_records for", name)
    print("done")


if __name__ == "__main__":
    run_test_add_records(items=record_tuples.all_record_generators)
