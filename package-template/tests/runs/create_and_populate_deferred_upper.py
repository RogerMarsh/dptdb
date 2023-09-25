# create_and_populate_deferred_upper.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate 'data_data_orv_inv_upper' database in file_definitions module.

This version of create_and_populate_deferred module exists to demonstrate
fastload is incompatible with field names which are not uppercase.

Just want one to reorganize in x86 and x64 environments.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

If default records is 65280 or less the run will succeed in x86 and x64
environments.

The run will succeed only in the x86 environment when default_records is
more than 65280.

"""
import multiprocessing

import create_and_populate_deferred
import file_definitions
import record_tuples


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    create_and_populate_deferred(
        file_definitions.DATA_DATA_ORD_INV_UPPER,
        file_definitions.data_data_ord_inv_upper,
        record_tuples.data_data_ord_inv_upper,
    )
