# run_test_populate_200000_record_databases_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate empty databases defined in file_definitions module.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

"""
import run_test_populate_databases_deferred


if __name__ == "__main__":
    run_test_populate_databases_deferred.run_test_populate_databases_deferred(
        default_records=200000
    )
