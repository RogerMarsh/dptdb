# run_test_multistep_sorting_discard.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate database with multi-step deferred update no forgivingness.

The records include alpha and numeric fields.

"""
import multiprocessing

import dptdb.dptapi

import record_tuples
import run_test_multistep_sort


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_multistep_sort.run_test_multistep_sort(
        btod_factor=256,  # 128 gets a 'Table D full response'.
        forgivingness=0,
        du_format_options=dptdb.dptapi.DU_FORMAT_DISCARD,
        ignore_discard=False,
        items=record_tuples.sorting_record_generators,
    )
