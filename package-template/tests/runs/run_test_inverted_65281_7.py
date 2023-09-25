# run_test_inverted_65281_7.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 7 records.

Use 65281 as default records with index values a function of record; and
set modulus as 9326 so most index values are used seven times and the
others six.

Change default records from 65280 used in the 65280_7 run written because
65281 causes the first record in the second segment to be created after
filling the first segment.

"""
import multiprocessing

import run_test_inverted_deferred
import record_tuples

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=65281,
        modulus=9326,
        deferred=False,
        items=record_tuples.record_generators,
    )
