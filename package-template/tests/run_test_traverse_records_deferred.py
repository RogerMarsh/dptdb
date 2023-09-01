# run_test_traverse_records_deferred.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to empty databases with ordered fields.

This module uses the same defaults as run_test_add_records module.  To
use defaults for list and bitmap inverted indicies run
'run_test_inverted_list_deferred' or 'run_test_inverted_bitmap_deferred'.

Use 200000 as default records with index values a function of record
number so all values refer to more than 10 records but less than 1000
records.  If there are more than 1000 records referenced in a segment,
a bitmap represents the list of records.

A 'run' function is defined for each definition in file_definitions module,
plus run_test_add_records which runs them all.

65537 records, not 200000, should be enough for this test because that is
where the ChessTab import fails in the x64 environment: the first segment
is full and a new segment is used.

However 200000 is exactly two orders of magnitude greater than the default
number of records and is enough to need four segments rather than one.

It is assumed the multiprocessing start method has been set as 'spawn'. 

"""
import multiprocessing

from dptdb import dptapi

import run_test_inverted_deferred as rtid
import add_records
import open_dpt_database
import file_definitions
import record_tuples
import filespec


def traverse_records(database, default_records, modulus):
    """Traverse database checking against default_records and modulus.

    The number of records that should be traversed is determined by
    default_records and modulus.

    """
    for file, context in database.contexts.items():

        # Find all records by EBM.
        foundset = context.FindRecords()

        try:
            assert foundset.Count() == default_records

            # Traverse in EBM forwards and backwards.
            for advance in (1, -1):
                cursor = foundset.OpenCursor()
                try:
                    count = 0
                    if advance == 1:
                        cursor.GotoFirst()
                    else:
                        cursor.GotoLast()
                    while True:
                        if not cursor.Accessible():
                            break
                        count += 1
                        cursor.Advance(advance)
                    assert count == default_records
                finally:
                    foundset.CloseCursor(cursor)
                    del cursor
            assert foundset.Count() == default_records

        finally:
            context.DestroyRecordSet(foundset)
            del foundset

        # Traverse fields in file and ignore non-ordered fields.
        fieldattrcursor = context.OpenFieldAttCursor()
        try:
            fieldattrcursor.GotoFirst()
            while True:
                if not fieldattrcursor.Accessible():
                    break
                attributes = fieldattrcursor.Atts()
                if not attributes.IsOrdered():
                    fieldattrcursor.Advance(1)
                    continue

                # Traverse index for each field forwards and backwards.
                for direction, valueadvance in (
                    (dptapi.CURSOR_ASCENDING, 1),
                    (dptapi.CURSOR_DESCENDING, -1),
                ):
                    fieldname = fieldattrcursor.Name()
                    valuecursor = context.OpenDirectValueCursor(
                        dptapi.APIFindValuesSpecification(fieldname)
                    )
                    try:
                        valuecursor.SetDirection(direction)
                        if valueadvance == 1:
                            valuecursor.GotoFirst()
                        else:
                            valuecursor.GotoLast()
                        while True:
                            if not valuecursor.Accessible():
                                break

                            # Traverse foundset for each field==value in
                            # index forwards and backwards.
                            foundset = context.FindRecords(
                                dptapi.APIFindSpecification(
                                    fieldname,
                                    dptapi.FD_EQ,
                                    dptapi.APIFieldValue(
                                        valuecursor.GetCurrentValue()
                                    )
                                )
                            )
                            assert foundset.Count() <= default_records
                            try:
                                for advance in (1, -1):
                                    cursor = foundset.OpenCursor()
                                    try:
                                        if advance == 1:
                                            cursor.GotoFirst()
                                        else:
                                            cursor.GotoLast()
                                        while True:
                                            if not cursor.Accessible():
                                                break
                                            cursor.Advance(advance)
                                    finally:
                                        foundset.CloseCursor(cursor)
                                        del cursor
                            finally:
                                context.DestroyRecordSet(foundset)
                                del foundset

                            valuecursor.Advance(valueadvance)
                    finally:
                        context.CloseDirectValueCursor(valuecursor)
                        del valuecursor
                fieldattrcursor.Advance(1)
        finally:
            context.CloseFieldAttCursor(fieldattrcursor)
            del fieldattrcursor


def populate_database_test_one_field_ordered(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.one_field_ordered(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )


def populate_database_two_field_one_ordered(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.two_field_one_ordered(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )


def populate_database_two_field_one_invisible(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.two_field_one_invisible(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )


def populate_database_three_field_one_invisible(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.three_field_one_invisible(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )


def populate_database_data_data_ord_inv(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    add_records.keep_records(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
        records=record_tuples.data_data_ord_inv(
            default_records=default_records,
            modulus=modulus,
        ),
        deferred=deferred,
    )


def rttrd_one_field_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Add records to database with one file and one ordered field.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=rtid.create_one_field_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    process = multiprocessing.Process(
        target=populate_database_test_one_field_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
            deferred=True,
            modulus=modulus,
        ),
    )
    process.start()
    process.join()
    database = open_dpt_database.open_dpt_database(
        file_definitions.ONE_FIELD_ORDERED,
        file_definitions.one_field_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records(database, default_records, modulus)
    database.delete()


def rttrd_two_field_one_ordered_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Add records to database one file, two fields one ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=rtid.create_two_field_one_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    process = multiprocessing.Process(
        target=populate_database_two_field_one_ordered,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
            deferred=True,
            modulus=modulus,
        ),
    )
    process.start()
    process.join()
    database = open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_ORDERED,
        file_definitions.two_field_one_ordered(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records(database, default_records, modulus)
    database.delete()


def rttrd_two_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Add records to database one file, two fields one invisible.

    Invisible possible only if ordered.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=rtid.create_two_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    process = multiprocessing.Process(
        target=populate_database_two_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
            deferred=True,
            modulus=modulus,
        ),
    )
    process.start()
    process.join()
    database = open_dpt_database.open_dpt_database(
        file_definitions.TWO_FIELD_ONE_INVISIBLE,
        file_definitions.two_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records(database, default_records, modulus)
    database.delete()


def rttrd_three_field_one_invisible_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Add records to database one file, three fields one invisible.

    That's two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=rtid.create_three_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    process = multiprocessing.Process(
        target=populate_database_three_field_one_invisible,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
            deferred=True,
            modulus=modulus,
        ),
    )
    process.start()
    process.join()
    database = open_dpt_database.open_dpt_database(
        file_definitions.THREE_FIELD_ONE_INVISIBLE,
        file_definitions.three_field_one_invisible(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records(database, default_records, modulus)
    database.delete()


def rttrd_data_data_ord_inv_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Add records to database one file, four fields one invisible.

    That's two unordered fields, two ordered fields, one of them invisible.

    Create a database large enough for default records and add that number
    of records to the database.

    """
    process = multiprocessing.Process(
        target=rtid.create_data_data_ord_inv,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    process.start()
    process.join()
    process = multiprocessing.Process(
        target=populate_database_data_data_ord_inv,
        kwargs=dict(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
            deferred=True,
            modulus=modulus,
        ),
    )
    process.start()
    process.join()
    database = open_dpt_database.open_dpt_database(
        file_definitions.DATA_DATA_ORD_INV,
        file_definitions.data_data_ord_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    traverse_records(database, default_records, modulus)
    database.delete()


def run_test_traverse_records_deferred(
    default_records=200, brecppg=50, btod_factor=1, modulus=None
):
    """Run tests for all the database definitions in file_definitions."""
    print(
        "enter run_test_traverse_records",
        "traversing",
        default_records,
        "records",
    )
    print("enter rttrd_one_field_ordered_deferred")
    rttrd_one_field_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
    )
    print("leave rttrd_one_field_ordered_deferred")
    print("enter rttrd_two_field_one_ordered_deferred")
    rttrd_two_field_one_ordered_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
    )
    print("leave rttrd_two_field_one_ordered_deferred")
    print("enter rttrd_two_field_one_invisible_deferred")
    rttrd_two_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
    )
    print("leave rttrd_two_field_one_invisible_deferred")
    print("enter rttrd_three_field_one_invisible_deferred")
    rttrd_three_field_one_invisible_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
    )
    print("leave rttrd_three_field_one_invisible_deferred")
    print("enter rttrd_data_data_ord_inv_deferred")
    rttrd_data_data_ord_inv_deferred(
        default_records=default_records,
        brecppg=brecppg,
        btod_factor=btod_factor,
        modulus=modulus,
    )
    print("leave rttrd_data_data_ord_inv_deferred")
    print("done")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_test_traverse_records_deferred()
