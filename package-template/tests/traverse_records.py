# traverse_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Various traverse record functions which may be sharable."""
import sys

from dptdb import dptapi

_MAXSIZE = sys.maxsize
del sys


def traverse_records(database, default_records=None, modulus=None):
    """Traverse database checking against default_records and modulus.

    The number of records that should be traversed is determined by
    default_records and modulus.

    """
    del modulus
    for file, context in database.contexts.items():

        # Find all records by EBM.
        foundset = context.FindRecords()

        try:
            if default_records is not None:
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
                    if default_records is not None:
                        assert count == default_records
                finally:
                    foundset.CloseCursor(cursor)
                    del cursor
            if default_records is not None:
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
                            if default_records is not None:
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


def traverse_records_trace(
    database,
    default_records=None,
    modulus=None,
    index_only=False,
    upper_count_limit=None,
    lower_count_limit=None,
    traverse_fields=None,
):
    """Traverse database with trace at Exception.

    The number of records that should be traversed is determined by
    default_records and modulus.

    """
    del modulus
    if upper_count_limit is None:
        upper_count_limit = default_records or _MAXSIZE
    if lower_count_limit is None:
        lower_count_limit = 0
    if traverse_fields is not None:
        traverse_fields = frozenset([t.lower() for t in traverse_fields])
    for file, context in database.contexts.items():
        if not index_only:
            foundset = context.FindRecords()
            try:
                if default_records is not None:
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
                if traverse_fields is not None:
                    if fieldname.lower() not in traverse_fields:
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
                                            recnum = _read_record(
                                                cursor
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


def traverse_records_read(database, default_records=None, modulus=None):
    """Traverse database checking against default_records and modulus.

    The number of records that should be traversed is determined by
    default_records and modulus.

    """
    del modulus
    for file, context in database.contexts.items():

        # Find all records by EBM.
        foundset = context.FindRecords()

        try:
            if default_records is not None:
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
                    if default_records is not None:
                        assert count == default_records
                finally:
                    foundset.CloseCursor(cursor)
                    del cursor
            if default_records is not None:
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
                            if default_records is not None:
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
                                            _read_fields(_read_record(cursor))
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


def _read_record(cursor):
    """Read record at current cursor location."""
    return cursor.AccessCurrentRecordForRead()


def _read_fields(record):
    """Read fields in record.

    Do nothing except exercise the advance loop.

    """
    while record.AdvanceToNextFVPair():
        pass
