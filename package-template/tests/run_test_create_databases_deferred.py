# run_test_create_databases_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module.

DPT files cannot be created and initialized in the same run as the file is
populated by deferred updates.

(Possibily not quite true because the DPT audit trail suggests the first
 file processed in such a run is populated before the job terminates
 without giving any failure indication.)

"""
import create_empty_database
import file_definitions


def run_test_one_file_no_fields_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and no fields.

    Create a dtatabase large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.ONE_FILE_NO_FIELDS,
        file_definitions.one_file_no_fields(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_one_file_one_field_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and one field.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_one_field_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_two_field_one_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_two_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_three_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_data_data_ord_inv_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records.

    """
    create_empty_database.create_empty_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    ).close_database()


def run_test_create_databases_deferred(
    default_records=200, brecppg=50, btod_factor=1
):
    """Run tests for all the database definitions in file_definitions."""
    print(
        "enter run_test_create_databases_deferred",
        "adding",
        default_records,
        "records",
    )
    print("enter run_test_one_file_no_fields_deferred")
    run_test_one_file_no_fields_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_file_no_fields_deferred")
    print("enter run_test_one_file_one_field_deferred")
    run_test_one_file_one_field_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_file_one_field_deferred")
    print("enter run_test_one_field_ordered_deferred")
    run_test_one_field_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_one_field_ordered_deferred")
    print("enter run_test_two_field_one_ordered_deferred")
    run_test_two_field_one_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_two_field_one_ordered_deferred")
    print("enter run_test_two_field_one_invisible_deferred")
    run_test_two_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_two_field_one_invisible_deferred")
    print("enter run_test_three_field_one_invisible_deferred")
    run_test_three_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_three_field_one_invisible_deferred")
    print("enter run_test_data_data_ord_inv_deferred")
    run_test_data_data_ord_inv_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
    )
    print("leave run_test_data_data_ord_inv_deferred")
    print("done")


if __name__ == "__main__":
    run_test_create_databases_deferred()
