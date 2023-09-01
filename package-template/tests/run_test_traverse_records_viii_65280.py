# run_test_traverse_records_viii_65280.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Traverse recordsets from run_test_vis_inv_inv_inv_65280_deferred run."""
import os

from dptdb import dptapi

import file_definitions
import dpt_database


def rttr_viii_65280(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    deferred=False,
    modulus=None,
    index_only=False,
    upper_count_limit=None,
    lower_count_limit=None,
):
    """Traverse an existing file."""

    if upper_count_limit is None:
        upper_count_limit = default_records
    if lower_count_limit is None:
        lower_count_limit = 0
    directory = dpt_database.directory_with_bitness()
    directory = os.path.join(directory, file_definitions.VIS_INV_INV_INV)
    database = dpt_database.DPTDatabase(
        directory,
        deferred=deferred,
        filedefs=file_definitions.vis_inv_inv_inv(
            default_records=default_records,
            brecppg=brecppg,
            btod_factor=btod_factor,
        ),
    )
    database.create()
    viewer_resetter = database.database_services.Core().GetViewerResetter()
    for file, context in database.contexts.items():
        if not index_only:
            foundset = context.FindRecords()
            try:
                assert foundset.Count() == default_records
                for advance in (1, -1):
                    cursor = foundset.OpenCursor()
                    ebm_count = 0
                    recnum = None
                    try:
                        if advance == 1:
                            cursor.GotoFirst()
                        else:
                            cursor.GotoLast()
                        while True:
                            if not cursor.Accessible():
                                break
                            ebm_count += 1
                            recnum = cursor.AccessCurrentRecordForRead(
                                ).RecNum()
                            cursor.Advance(advance)
                    except RuntimeError as exc:
                        print("ebm advance", advance, ebm_count)
                        print("recnum", recnum)
                        raise
                    finally:
                        foundset.CloseCursor(cursor)
                        del cursor
            finally:
                context.DestroyRecordSet(foundset)
                del foundset
        fieldattrcursor = context.OpenFieldAttCursor()
        try:
            fa_count = 0
            fieldattrcursor.GotoFirst()
            while True:
                if not fieldattrcursor.Accessible():
                    break
                attributes = fieldattrcursor.Atts()
                if not attributes.IsOrdered():
                    fa_count += 1
                    fieldattrcursor.Advance(1)
                    continue
                fieldname = fieldattrcursor.Name()
                if fieldname.lower() != file_definitions.FLDORD:
                    fa_count += 1
                    fieldattrcursor.Advance(1)
                    continue
                for vc_direction, vc_advance in (
                    (dptapi.CURSOR_ASCENDING, 1),
                    (dptapi.CURSOR_DESCENDING, -1),
                ):
                    valuecursor = context.OpenDirectValueCursor(
                        dptapi.APIFindValuesSpecification(fieldname)
                    )
                    v_count = 0
                    try:
                        valuecursor.SetDirection(vc_direction)
                        valuecursor.GotoFirst()
                        while True:
                            if not valuecursor.Accessible():
                                break
                            if index_only:
                                v_count += 1
                                valuecursor.Advance(vc_advance)
                                continue
                            foundset = context.FindRecords(
                                dptapi.APIFindSpecification(
                                    fieldname,
                                    dptapi.FD_EQ,
                                    dptapi.APIFieldValue(
                                        valuecursor.GetCurrentValue()
                                    )
                                )
                            )
                            foundset_count = foundset.Count()
                            try:
                                if (
                                    foundset_count > upper_count_limit or
                                    foundset_count < lower_count_limit
                                ):
                                    v_count += 1
                                    valuecursor.Advance(vc_advance)
                                    continue
                                for advance in (1, -1):
                                    cursor = foundset.OpenCursor()
                                    adv_count = 0
                                    recnum = None
                                    try:
                                        if advance == 1:
                                            cursor.GotoFirst()
                                        else:
                                            cursor.GotoLast()
                                        while True:
                                            if not cursor.Accessible():
                                                break
                                            adv_count += 1
                                            recnum = cursor.AccessCurrentRecordForRead(
                                                ).RecNum()
                                            cursor.Advance(advance)
                                    except RuntimeError as exc:
                                        print("advance", advance, adv_count)
                                        print("recnum", recnum)
                                        print("field", fieldname, fa_count)
                                        print(
                                            "value",
                                            valuecursor.GetCurrentValue(
                                                ).ExtractString(),
                                            v_count,
                                        )
                                        print(
                                            "vc_advance",
                                            vc_advance,
                                            v_count,
                                        )
                                        print(
                                            "recordset count",
                                            foundset_count,
                                        )
                                        raise
                                    finally:
                                        foundset.CloseCursor(cursor)
                                        del cursor
                            finally:
                                context.DestroyRecordSet(foundset)
                                del foundset
                            v_count += 1
                            valuecursor.Advance(vc_advance)
                    finally:
                        context.CloseDirectValueCursor(valuecursor)
                        del valuecursor
                fa_count += 1
                fieldattrcursor.Advance(1)
        finally:
            context.CloseFieldAttCursor(fieldattrcursor)
            del fieldattrcursor
    database.close_database()


def run_test_traverse_records_viii_65280(
    default_records=200,
    brecppg=50,
    btod_factor=1,
    modulus=None,
    deferred=False,
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
        deferred=deferred,
        modulus=modulus,
        index_only=index_only,
        upper_count_limit=upper_count_limit,
        lower_count_limit=lower_count_limit,
    )


if __name__ == "__main__":
    run_test_traverse_records_viii_65280(
        default_records=65280, modulus=13, btod_factor=400
    )
