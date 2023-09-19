# run_test_create_and_populate_200000_502.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create and populate a database for run_test_reorganize.

This is known to work in x86 environment, but not x64, due to the
record profile.

"""
import multiprocessing

import create_and_populate_deferred


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    create_and_populate_deferred.create_and_populate_deferred(
        default_records=200000, modulus=130
    )
