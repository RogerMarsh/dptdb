# run_test_populate_databases_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_populate_databases_deferred which runs them all.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

All field values are unique in these tests, so lists and bitmaps are not
used to implement the inverted lists of records.

65537 records, not 200000, should be enough for this test because that is
where the ChessTab import fails in the x64 environment: the first segment
is full and a new segment is used.

However 200000 is exactly two orders of magnitude greater than the default
number of records and is enough to need four segments rather than one.

The only bitmap in use is the existence bitmap: this module tests if there
is a problem creating more than one existence bitmap segment in the x64
environment.

"""
import run_test_add_records
import file_definitions


def rtpdd_one_file_no_fields_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database with one file and no fields."""
    run_test_add_records.rtar_one_file_no_fields(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_one_file_one_field_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database with one file and one field."""
    run_test_add_records.rtar_one_file_one_field(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_one_field_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database with one file and one ordered field."""
    run_test_add_records.rtar_one_field_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_two_field_one_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database one file, two fields one ordered."""
    run_test_add_records.rtar_two_field_one_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_two_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    """
    run_test_add_records.rtar_two_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_three_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    """
    run_test_add_records.rtar_three_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtpdd_data_data_ord_inv_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add default_records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    """
    run_test_add_records.rtar_data_data_ord_inv(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def run_test_populate_databases_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Run tests for all the database definitions in file_definitions."""
    print(
        "enter run_test_add_records_deferred",
        "adding",
        default_records,
        "records",
    )
    print("enter rtpdd_one_file_no_fields_deferred")
    rtpdd_one_file_no_fields_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_one_file_no_fields_deferred")
    print("enter rtpdd_one_file_one_field_deferred")
    rtpdd_one_file_one_field_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_one_file_one_field_deferred")
    print("enter rtpdd_one_field_ordered_deferred")
    rtpdd_one_field_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_one_field_ordered_deferred")
    print("enter rtpdd_two_field_one_ordered_deferred")
    rtpdd_two_field_one_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_two_field_one_ordered_deferred")
    print("enter rtpdd_two_field_one_invisible_deferred")
    rtpdd_two_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_two_field_one_invisible_deferred")
    print("enter rtpdd_three_field_one_invisible_deferred")
    rtpdd_three_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_three_field_one_invisible_deferred")
    print("enter rtpdd_data_data_ord_inv_deferred")
    rtpdd_data_data_ord_inv_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtpdd_data_data_ord_inv_deferred")
    print("done")


if __name__ == "__main__":
    run_test_populate_databases_deferred()
