# run_test_inverted.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields.

The update is done in normal mode by calling the

run_test_inverted_deferred.run_test_inverted_deferred function with

argument 'deferred' set False.

"""
import multiprocessing

import run_test_inverted_deferred
import record_tuples

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        deferred=False,
        items=record_tuples.record_generators,
    )
