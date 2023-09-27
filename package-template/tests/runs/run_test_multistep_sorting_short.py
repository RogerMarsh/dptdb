# run_test_multistep_sorting_short.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate database with multi-step deferred update no forgivingness.

The records include alpha and numeric fields.

Set du_fixed_length=10 which is less than longest ORD NUM index value
length, 17, reported in 'DPT.3109' message.

"""
import multiprocessing

import record_tuples
import run_test_multistep_sort


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_multistep_sort.run_test_multistep_sort(
        btod_factor=256,  # 128 gets a 'Table D full response'.
        forgivingness=0,
        du_fixed_length=10,
        items=record_tuples.sorting_record_generators,
    )
