# create_and_populate_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate 'data_data_orv_inv' database defined in file_definitions module.

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


def create_and_populate_deferred(
    name,
    definition,
    records,
    default_records=200,
    modulus=None,
):
    """Create and populate the database."""
    process = multiprocessing.Process(
        target=open_dpt_database.create_database,
        args=(name, definition),
        kwargs=dict(default_records=default_records),
    )
    process.start()
    process.join()

    add_records.keep_records(
        name,
        definition(default_records=default_records),
        records=records,
        default_records=default_records,
        modulus=modulus,
        deferred=True,
    )


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")

    create_and_populate_deferred(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv,
        record_tuples.data_data_ord_inv,
    )
