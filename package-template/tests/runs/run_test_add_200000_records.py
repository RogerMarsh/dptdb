# run_test_add_200000_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases defined in file_definitions module.

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


if __name__ == "__main__":
    run_test_add_records.run_test_add_records(default_records=200000)
