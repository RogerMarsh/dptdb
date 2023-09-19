# reorganize_x64_200000_502_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Reorganize database defined in file_definitions module.

This is known to work in x86 environment, although best to verify the
run can work: the test is what about x64.

"""
import open_dpt_database
import file_definitions


if __name__ == "__main__":
    database = open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(),
    )
    print("start reorganize_x64_200000_502_deferred")
    try:
        for file, context in database.contexts.items():
            print("enter reorganize for", file)
            context.Reorganize()
            print("leave reorganize for", file)
        print("finish reorganize_x64_200000_502_deferred")
    finally:
        database.close_database()
