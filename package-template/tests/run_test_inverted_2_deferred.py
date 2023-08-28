# run_test_inverted_2_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 2 records.

Use 200, the default, as default records with index values a function of
record; and set modulus as 100 so each index value is used twice.

"""
import multiprocessing

import run_test_inverted_deferred

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(modulus=100)
