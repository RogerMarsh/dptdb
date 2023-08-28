# run_test_add_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

All field values are unique in these tests, so lists and bitmaps are not
used to implement the inverted lists of records.

"""
import file_definitions
import record_tuples
import add_records


def run_test_one_file_no_fields(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database with one file and no fields.

    Create a dtatabase large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.ONE_FILE_NO_FIELDS,
        file_definitions.one_file_no_fields(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.one_file_no_fields(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_one_file_one_field(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database with one file and one field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.one_file_one_field(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_one_field_ordered(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.one_field_ordered(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_two_field_one_ordered(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.two_field_one_ordered(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_two_field_one_invisible(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.two_field_one_invisible(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_three_field_one_invisible(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.three_field_one_invisible(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_data_data_ord_inv(
    default_records=200, brecppg=50, btod_factor=1, deferred=False
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.add_records(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.data_data_ord_inv(
            default_records=default_records
        ),
        deferred=deferred,
    )


def run_test_add_records(default_records=200, brecppg=50, btod_factor=1):
    """Run tests for all the database definitions in file_definitions."""
    print("enter run_test_add_records", "adding", default_records, "records")
    print("enter run_test_one_file_no_fields")
    run_test_one_file_no_fields(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_file_no_fields")
    print("enter run_test_one_file_one_field")
    run_test_one_file_one_field(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_file_one_field")
    print("enter run_test_one_field_ordered")
    run_test_one_field_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_field_ordered")
    print("enter run_test_two_field_one_ordered")
    run_test_two_field_one_ordered(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_two_field_one_ordered")
    print("enter run_test_two_field_one_invisible")
    run_test_two_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_two_field_one_invisible")
    print("enter run_test_three_field_one_invisible")
    run_test_three_field_one_invisible(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_three_field_one_invisible")
    print("enter run_test_data_data_ord_inv")
    run_test_data_data_ord_inv(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_data_data_ord_inv")


if __name__ == "__main__":
    run_test_add_records()
