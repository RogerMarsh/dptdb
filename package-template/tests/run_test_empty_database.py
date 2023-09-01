# run_test_empty_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create and delete empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_empty_database which runs them all.

"""
import open_dpt_database
import file_definitions


def _rted_empty_database(name, definition, directory=None):
    """Create and delete database with definition in directory/name."""
    database = open_dpt_database.open_dpt_database(
        name, definition, directory=directory
    )
    database.delete()


def rted_one_file_no_fields():
    """Create and delete database with one file and no fields."""
    _rted_empty_database(
        file_definitions.ONE_FILE_NO_FIELDS,
        file_definitions.one_file_no_fields(),
    )


def rted_one_file_one_field():
    """Create and delete database with one file and one field."""
    _rted_empty_database(
        file_definitions.ONE_FILE_ONE_FIELD,
        file_definitions.one_file_one_field(),
    )


def rted_one_field_ordered():
    """Create and delete database with one file and one ordered field."""
    _rted_empty_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(),
    )


def rted_two_field_one_ordered():
    """Create and delete database one file, two fields one ordered."""
    _rted_empty_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(),
    )


def rted_two_field_one_invisible():
    """Create and delete database one file, two fields one invisible.

    Invisible possible only if ordered.

    """
    _rted_empty_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(),
    )


def rted_three_field_one_invisible():
    """Create and delete database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    """
    _rted_empty_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(),
    )


def rted_data_data_ord_inv():
    """Create and delete database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    """
    _rted_empty_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(),
    )


def run_test_empty_database():
    """Run tests for all the database definitions in file_definitions."""
    print("start ")
    print("enter rted_one_file_no_fields")
    rted_one_file_no_fields()
    print("leave rted_one_file_no_fields")
    print("enter rted_one_file_one_field")
    rted_one_file_one_field()
    print("leave rted_one_file_one_field")
    print("enter rted_one_field_ordered")
    rted_one_field_ordered()
    print("leave rted_one_field_ordered")
    print("enter rted_two_field_one_ordered")
    rted_two_field_one_ordered()
    print("leave rted_two_field_one_ordered")
    print("enter rted_two_field_one_invisible")
    rted_two_field_one_invisible()
    print("leave rted_two_field_one_invisible")
    print("enter rted_three_field_one_invisible")
    rted_three_field_one_invisible()
    print("leave rted_three_field_one_invisible")
    print("enter rted_data_data_ord_inv")
    rted_data_data_ord_inv()
    print("leave rted_data_data_ord_inv")
    print("done")


if __name__ == "__main__":
    run_test_empty_database()
