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

import open_dpt_database
import file_definitions
import add_records
import record_tuples


def _create(default_records=200):
    """Create the database in a normal session."""
    open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV_UPPER,
        file_definitions.data_data_ord_inv_upper(
            default_records=default_records
        ),
    ).close_database()


def _populate(default_records=200, modulus=None):
    """Add default_records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    """
    add_records.keep_records(
        file_definitions.DATA_DATA_ORD_INV_UPPER,
        file_definitions.data_data_ord_inv_upper(
            default_records=default_records
        ),
        records=record_tuples.data_data_ord_inv_upper(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=True,
    )


def create_and_populate_deferred_upper(default_records=200, modulus=None):
    """Create and populate the database."""
    process = multiprocessing.Process(
        target=_create,
        kwargs=dict(default_records=default_records),
    )
    process.start()
    process.join()
    _populate(default_records=default_records, modulus=modulus)


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    create_and_populate_deferred_upper()
