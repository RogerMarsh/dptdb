# run_test_inverted_200004_7_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases where index values refer to 7 records.

Use 200004 as default records with index values a function of record; and
set modulus as 28572 so each index value is used seven times.

Change default records from 200000 used in runs written earlier because
it turns out that having index values refer to seven records, rather than
six, introduces the x64 crash.  (200004 % [2|6|7] == 0).

Note that 200000 as default_records uses the available record numbers but
there are 46 unused record numbers for 200004 (an extra Table B page is
created for the extra four records: 200000 // 50 == 200004 // 50 == 4000)

"""
import multiprocessing

import run_test_inverted_deferred

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred.run_test_inverted_deferred(
        default_records=200004, modulus=28572
    )
