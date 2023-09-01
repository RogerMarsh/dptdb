# run_test_inverted_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields.

This module uses the same defaults as run_test_add_records module.  To
use defaults for list and bitmap inverted indicies run
'run_test_inverted_list_deferred' or 'run_test_inverted_bitmap_deferred'.

Use 200000 as default records with index values a function of record
number so all values refer to more than 10 records but less than 1000
records.  If there are more than 1000 records referenced in a segment,
a bitmap represents the list of records.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

65537 records, not 200000, should be enough for this test because that is
where the ChessTab import fails in the x64 environment: the first segment
is full and a new segment is used.

However 200000 is exactly two orders of magnitude greater than the default
number of records and is enough to need four segments rather than one.

It is assumed the multiprocessing start method has been set as 'spawn'. 

"""
import multiprocessing

import run_test_add_records
import open_dpt_database
import file_definitions


def create_one_field_ordered(
    default_records=200, brecppg=50, btod_factor=1
):
    """Create a database large enough for default records.

    Provided for convenient use wia multiprocessing.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def create_two_field_one_ordered(
    default_records=200, brecppg=50, btod_factor=1
):
    """Create a database large enough for default records.

    Provided for convenient use wia multiprocessing.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def create_two_field_one_invisible(
    default_records=200, brecppg=50, btod_factor=1
):
    """Create a database large enough for default records.

    Provided for convenient use wia multiprocessing.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def create_three_field_one_invisible(
    default_records=200, brecppg=50, btod_factor=1
):
    """Create a database large enough for default records.

    Provided for convenient use wia multiprocessing.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def create_data_data_ord_inv(
    default_records=200, brecppg=50, btod_factor=1
):
    """Create a database large enough for default records.

    Provided for convenient use wia multiprocessing.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def rtid_one_field_ordered_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=create_one_field_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    run_test_add_records.rtar_one_field_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=deferred,
        modulus=modulus,
    )


def rtid_two_field_one_ordered_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=create_two_field_one_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    run_test_add_records.rtar_two_field_one_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=deferred,
        modulus=modulus,
    )


def rtid_two_field_one_invisible_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=create_two_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    run_test_add_records.rtar_two_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=deferred,
        modulus=modulus,
    )


def rtid_three_field_one_invisible_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=create_three_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    run_test_add_records.rtar_three_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=deferred,
        modulus=modulus,
    )


def rtid_data_data_ord_inv_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=create_data_data_ord_inv,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    run_test_add_records.rtar_data_data_ord_inv(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=deferred,
        modulus=modulus,
    )


def run_test_inverted_deferred(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=True,
):
    """Run tests for all the database definitions in file_definitions."""
    print(
        "enter run_test_inverted_deferred",
        "(deferred is " + str(deferred) + ")",
        "adding",
        default_records,
        "records",
    )
    print("enter rtid_one_field_ordered_deferred")
    rtid_one_field_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        deferred=deferred,
    )
    print("leave rtid_one_field_ordered_deferred")
    print("enter rtid_two_field_one_ordered_deferred")
    rtid_two_field_one_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        deferred=deferred,
    )
    print("leave rtid_two_field_one_ordered_deferred")
    print("enter rtid_two_field_one_invisible_deferred")
    rtid_two_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        deferred=deferred,
    )
    print("leave rtid_two_field_one_invisible_deferred")
    print("enter rtid_three_field_one_invisible_deferred")
    rtid_three_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        deferred=deferred,
    )
    print("leave rtid_three_field_one_invisible_deferred")
    print("enter rtid_data_data_ord_inv_deferred")
    rtid_data_data_ord_inv_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        deferred=deferred,
    )
    print("leave rtid_data_data_ord_inv_deferred")
    print("done")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_inverted_deferred()
