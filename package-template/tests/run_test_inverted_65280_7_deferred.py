# run_test_inverted_65280_7_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 7 records.

Use 65280 as default records with index values a function of record; and
set modulus as 9326 so most index values are used seven times and the
others six.

Change default records from 200004 used in the 200004_7 run written because
65280 is the number of records which fit in one segment.

"""
import multiprocessing

import run_test_inverted_deferred

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=65280, modulus=9326
    )
