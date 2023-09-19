# create_x86_200000_502_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Populate database defined in file_definitions module.

Just want one to reorganize in x64 environment.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

"""
import run_test_create_databases


if __name__ == "__main__":
    print("start create_x86_200000_502_deferred")
    run_test_create_databases.rtcd_data_data_ord_inv(
        default_records=200000, modulus=130
    )
    print("finish create_x86_200000_502_deferred")
