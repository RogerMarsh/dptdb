# run_test_traverse_6_viii_65280.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Traverse recordsets from run_test_vis_inv_inv_inv_65280_deferred run.

Recordsets for index values with more than 6 records are excluded,

This should exclude bitmap and large list representations of inverted
lists.

The 'Bit subscript out of mapped range' Runtime Error does not occur.

"""
import run_test_traverse_records_viii_65280

if __name__ == "__main__":
    run_test_traverse_records_viii_65280.rttr_viii_65280(
        default_records=65280,
        modulus=13,
        btod_factor=400,
        upper_count_limit=6
    )
