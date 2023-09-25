# run_test_traverse_records_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields.

This module uses the same defaults as run_test_add_records module.  To
use defaults for list and bitmap inverted indicies run
'run_test_inverted_list_deferred' or 'run_test_inverted_bitmap_deferred'.

Use 200000 as default records with index values a function of record
number so all values refer to more than 10 records but less than 1000
records.  If there are more than 1000 records referenced in a segment,
a bitmap represents the list of records.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

65537 records, not 200000, should be enough for this test because that is
where the ChessTab import fails in the x64 environment: the first segment
is full and a new segment is used.

However 200000 is exactly two orders of magnitude greater than the default
number of records and is enough to need four segments rather than one.

It is assumed the multiprocessing start method has been set as 'spawn'. 

"""
import multiprocessing

from dptdb import dptapi

import add_records
import open_dpt_database
import record_tuples
import traverse_records


def run_test_traverse_records_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None, items=None
):
    """Run tests for all the database definitions in file_definitions."""
    if items is None:
        items = ()
    print(
        "enter run_test_traverse_records",
        "traversing",
        default_records,
        "records",
    )
    for name, definition, records in items:
        print("enter for", name)
        process = multiprocessing.Process(
            target=open_dpt_database.create_database,
            args=(
                name,
                definition,
            ),
            kwargs=dict(
                default_records=default_records,
                brecppg=brecppg,
                btod_factor=btod_factor,
            ),
        )
        process.start()
        process.join()
        process = multiprocessing.Process(
            target=add_records.keep_records,
            args=(
                name,
                definition(
                    default_records=default_records,
                    brecppg=brecppg,
                    btod_factor=btod_factor,
                ),
            ),
            kwargs=dict(
                records=records,
                default_records=default_records,
                deferred=True,
                modulus=modulus,
            ),
        )
        process.start()
        process.join()
        database = open_dpt_database.open_dpt_database(
            name,
            definition(
                default_records=default_records,
                brecppg=brecppg,
                btod_factor=btod_factor,
            ),
        )
        traverse_records.traverse_records(
            database, default_records=default_records, modulus=modulus
        )
        database.delete()
        print("leave for", name)
    print("done")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_traverse_records_deferred(items=record_tuples.record_generators)
