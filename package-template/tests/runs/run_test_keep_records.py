# run_test_keep_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

All field values are unique in these tests, so lists and bitmaps are not
used to implement the inverted lists of records.

"""
import record_tuples
import add_records


def run_test_keep_records(
    name,
    definition,
    records,
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    multistep=False,
    modulus=None,
    du_fixed_length=-1,  # OpenContext_DUMulti du_parm3 argument.
    du_format_options=None,  # OpenContext_DUMulti du_parm4 argument.
):
    """Add records to database for name and definition.

    Create a dtatabase large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        name,
        definition(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=records,
        deferred=deferred,
        multistep=multistep,
        du_fixed_length=du_fixed_length,
        du_format_options=du_format_options,
    )


if __name__ == "__main__":
    print("run_test_keep_records adding 200 records")
    for name, definition, records in record_tuples.all_record_generators:
        print("enter run_test_keep_records for", name)
        run_test_keep_records(
            name,
            definition,
            records,
        )
        print("leave run_test_keep_records")
