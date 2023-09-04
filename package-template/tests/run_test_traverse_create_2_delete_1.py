# run_test_create_2_delete_1.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add 2 records to database without ordered fields and delete record 0.

This does not cause RuntimeError 'Bit subscript out of mapped range'.

Assumption is inverted lists are not involved because there is only one
record on the database when the recordset is traversed; even though the
Existence Bit Map is never not a bit map implying the derived foundset
is neither list nor bitmap representation of an inverted list in this
case.

"""
import run_test_traverse_create_3_delete_1


def run_test_traverse_create_2_delete_1():
    run_test_traverse_create_3_delete_1.rttc3d1_one_file_one_field(
        default_records=2
    )
    print("run_test_create_2_delete_1", "done")


if __name__ == "__main__":
    run_test_traverse_create_2_delete_1()
