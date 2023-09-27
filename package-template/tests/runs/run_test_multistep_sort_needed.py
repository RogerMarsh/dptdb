# run_test_multistep_sort_needed.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate database with multi-step deferred update no forgivingness.

This run should crash reporting 'too many unsorted records': no point
in following run_test_multistep_no_sort and having five crashes, one
will do.

"""
import multiprocessing

import record_tuples
import run_test_multistep_no_sort


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_multistep_no_sort.run_test_multistep_no_sort(
        forgivingness=0,
        items=record_tuples.record_generators,
    )
