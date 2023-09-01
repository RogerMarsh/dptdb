# run_test_traverse_index_viii_65280.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Traverse indicies from run_test_vis_inv_inv_inv_65280_deferred run."""
import run_test_traverse_records_viii_65280

if __name__ == "__main__":
    run_test_traverse_records_viii_65280.rttr_viii_65280(
        default_records=65280, modulus=13, btod_factor=400, index_only=True
    )
