# run_test_traverse_records_viii_65280.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Traverse recordsets from run_test_vis_inv_inv_inv_65280_deferred run."""
import file_definitions
import open_dpt_database
import traverse_records


def rttr_viii_65280(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    index_only=False,
    upper_count_limit=None,
    lower_count_limit=None,
):
    """Traverse an existing file."""

    database = open_dpt_database.open_dpt_database(
        file_definitions.VIS_INV_INV_INV,
        file_definitions.vis_inv_inv_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records.traverse_records_trace(
        database,
        default_records=default_records,
        modulus=modulus,
        index_only=index_only,
        upper_count_limit=upper_count_limit,
        lower_count_limit=lower_count_limit,
        traverse_fields=(file_definitions.FLDORD,),
    )
    database.close_database()


def run_test_traverse_records_viii_65280(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    index_only=False,
    upper_count_limit=None,
    lower_count_limit=None,
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    rttr_viii_65280(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
        index_only=index_only,
        upper_count_limit=upper_count_limit,
        lower_count_limit=lower_count_limit,
    )


if __name__ == "__main__":
    run_test_traverse_records_viii_65280(
        default_records=65280, modulus=13, btod_factor=400
    )
    print("run_test_traverse_records_viii_65280", "done")
