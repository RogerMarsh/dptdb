# run_test_traverse_4_2_records_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields.

The smallest database with multiple references to each record where some
index values have record number 0 as first record and others have record
number 1 as first record.

"""
import multiprocessing

import run_test_traverse_records_deferred
import record_tuples

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_traverse_records_deferred.run_test_traverse_records_deferred(
        default_records=4,
        modulus=2,
        items=record_tuples.record_generators,
    )
