# run_test_inverted_65280_5021_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 5021 records.

Use 65280 as default records with index values a function of record; and
set modulus as 13 so most index values are used 5021 times and the others
5020.

5021 is a more than large enough list of record numbers (about a 1000
would do) for it to be a bitmap.

"""
import multiprocessing

import run_test_inverted_deferred
import record_tuples

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=65280,
        modulus=13,
        items=record_tuples.record_generators,
    )
