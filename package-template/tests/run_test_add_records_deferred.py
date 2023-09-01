# run_test_add_records_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

THIS MODULE DOES NOT DO IT'S TASK, because:

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

and exists only because run_test_add_records.py exists.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

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
import open_dpt_database
import file_definitions


def rtard_one_file_no_fields_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and no fields.

    Create a dtatabase large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.ONE_FILE_NO_FIELDS,
        file_definitions.one_file_no_fields(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_one_file_no_fields(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_one_file_one_field_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and one field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_one_file_one_field(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_one_field_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_one_field_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_two_field_one_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_two_field_one_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_two_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_two_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_three_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_three_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def rtard_data_data_ord_inv_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()
    run_test_add_records.rtar_data_data_ord_inv(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        deferred=True,
    )


def run_test_add_records_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Run tests for all the database definitions in file_definitions."""
    print("WARNING:    This run cannot succeed.")
    print("WARNING:    The DPT stuff for first file is done but the 'leave'")
    print("WARNING:    trace message does not get printed; and the run")
    print("WARNING:    terminates without giving any failure indication.")
    print("WARNING:    (compare with similar 'run_test_add_records' job)")
    print("WARNING:    Use 'run_test_create_databases' followed")
    print("WARNING:     by 'run_test_populate_databases_deferred' instead.")
    print(
        "enter run_test_add_records_deferred",
        "adding",
        default_records,
        "records",
    )
    print("enter rtard_one_file_no_fields_deferred")
    rtard_one_file_no_fields_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_one_file_no_fields_deferred")
    print("enter rtard_one_file_one_field_deferred")
    rtard_one_file_one_field_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_one_file_one_field_deferred")
    print("enter rtard_one_field_ordered_deferred")
    rtard_one_field_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_one_field_ordered_deferred")
    print("enter rtard_two_field_one_ordered_deferred")
    rtard_two_field_one_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_two_field_one_ordered_deferred")
    print("enter rtard_two_field_one_invisible_deferred")
    rtard_two_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_two_field_one_invisible_deferred")
    print("enter rtard_three_field_one_invisible_deferred")
    rtard_three_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_three_field_one_invisible_deferred")
    print("enter rtard_data_data_ord_inv_deferred")
    rtard_data_data_ord_inv_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave rtard_data_data_ord_inv_deferred")
    print("done")


if __name__ == "__main__":
    run_test_add_records_deferred()
