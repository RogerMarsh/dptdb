# run_test_inverted_list_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases such that lists implement indicies.

Use 200000 as default records with index values a function of record
number so all values refer to more than 10 records but less than 1000
records.  If there are more than 1000 records referenced in a segment,
a bitmap represents the list of records.

Set modulus to 1023 so each index value references just under 200 records.

"""
import multiprocessing

import run_test_inverted_deferred

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=200000, modulus=1023
    )
