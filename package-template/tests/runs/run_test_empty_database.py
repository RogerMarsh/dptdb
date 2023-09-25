# run_test_empty_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create and delete empty databases defined in file_definitions module.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_empty_database which runs them all.

"""
import open_dpt_database
import record_tuples


def run_test_empty_database(directory=None, items=None):
    """Run tests for all the database definitions in file_definitions."""
    if items is None:
        items = ()
    print("enter run_test_empty_database")
    for name, definition, records in items:
        del records
        print("enter open_dpt_database then delete for", name)
        database = open_dpt_database.open_dpt_database(
            name, definition(), directory=directory
        )
        database.delete()
        print("leave open_dpt_database then delete for", name)
    print("leave run_test_empty_database")
    print("done")


if __name__ == "__main__":
    run_test_empty_database(items=record_tuples.all_record_generators)
