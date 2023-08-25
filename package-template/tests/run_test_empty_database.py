# run_test_empty_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create and delete empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_empty_database which runs them all.

"""
import sys
import os
    
import dpt_database
import file_definitions

# See documentation for platform module.
is_64bits = sys.maxsize > 2 ** 32


def directory_with_bitness(directory):
    """Return directory with 'bitness' of Python interpreter appended."""
    return directory + ("64" if is_64bits else "32")


def _run_test_empty_database(name, definition, directory=None):
    """Create and delete database with definition in directory/name."""
    if directory is None:
        directory = os.environ.get(
            "TEMP",
            os.environ.get("TMP",os.environ.get("HOME")),
        )
        directory = directory_with_bitness(directory)
    directory = os.path.join(directory, name)
    database = dpt_database.DPTDatabase(directory, filedefs=definition)
    database.create()
    database.delete()


def run_test_one_file_no_fields():
    """Create and delete database with one file and no fields."""
    _run_test_empty_database(
        file_definitions.ONE_FILE_NO_FIELDS,
        file_definitions.one_file_no_fields,
    )


def run_test_one_file_one_field():
    """Create and delete database with one file and one field."""
    _run_test_empty_database(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field,
    )


def run_test_one_field_ordered():
    """Create and delete database with one file and one ordered field."""
    _run_test_empty_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered,
    )


def run_test_two_field_one_ordered():
    """Create and delete database one file, two fields one ordered."""
    _run_test_empty_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered,
    )


def run_test_two_field_one_invisible():
    """Create and delete database one file, two fields one invisible.

    Invisible possible only if ordered.

    """
    _run_test_empty_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible,
    )


def run_test_three_field_one_invisible():
    """Create and delete database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    """
    _run_test_empty_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible,
    )


def run_test_data_data_ord_inv():
    """Create and delete database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    """
    _run_test_empty_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv,
    )


def run_test_empty_database():
    """Run tests for all the database definitions in file_definitions."""
    run_test_one_file_no_fields()
    run_test_one_file_one_field()
    run_test_one_field_ordered()
    run_test_two_field_one_ordered()
    run_test_two_field_one_invisible()
    run_test_three_field_one_invisible()
    run_test_data_data_ord_inv()


if __name__ == "__main__":
    run_test_empty_database()
