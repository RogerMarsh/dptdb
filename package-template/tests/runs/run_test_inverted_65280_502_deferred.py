# run_test_inverted_65280_502_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 502 records.

Use 65280 as default records with index values a function of record; and
set modulus as 130 so most index values are used 502 times and the others
501.

502 is a large list of record numbers, but not yet large enough to be a
bitmap, compared with 6 which is the largest small list.

"""
import multiprocessing

import run_test_inverted_deferred

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=65280, modulus=130
    )
