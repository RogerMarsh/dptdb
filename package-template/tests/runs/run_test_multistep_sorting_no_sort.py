# run_test_multistep_sorting_no_sort.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate database with multi-step deferred update full forgivingness.

The records include alpha and numeric fields.

"""
import multiprocessing

import dptdb.dptapi

import record_tuples
import run_test_multistep_no_sort


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_multistep_no_sort.run_test_multistep_no_sort(
        btod_factor=256,  # 128 gets a 'Table D full response'.
        items=record_tuples.sorting_record_generators,
    )
