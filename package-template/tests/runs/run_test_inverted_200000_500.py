# run_test_inverted_200000_500.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 500 records.

Use 200000 as default records with index values a function of record; and
set modulus as 400 so each index value is used 500 times (over 100 times
per segment except the last).  Not enough for any bitmaps.

Introduced after seeing run_test_inversted_65281_7 succeed.

"""
import multiprocessing

import run_test_inverted_deferred
import record_tuples

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=200000,
        modulus=400,
        deferred=False,
        items=record_tuples.record_generators,
    )
