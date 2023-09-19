# run_test_create_and_populate_upper_200000_502.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create and populate a database for run_test_reorganize.

This is known to work in x86 environment, but not x64, due to the
record profile.

This version of run_test_create_and_populate_200000_502 module exists to
demonstrate fastload is incompatible with field names which are not
uppercase.

"""
import multiprocessing

import create_and_populate_deferred_upper


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    create_and_populate_deferred_upper.create_and_populate_deferred_upper(
        default_records=200000, modulus=130
    )
