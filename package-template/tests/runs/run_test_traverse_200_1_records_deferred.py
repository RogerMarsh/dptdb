# run_test_traverse_200_1_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields."""
import multiprocessing

import run_test_traverse_records_deferred


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_traverse_records_deferred.run_test_traverse_records_deferred(
        modulus=1)
