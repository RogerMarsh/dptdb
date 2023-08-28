# record_tuples.py
# Copyright 2023 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Define sample FileSpec instances for tests."""
import filespec as fs
import file_definitions as fd


def one_file_no_fields(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        for i in range(default_records):
            yield ()

    return value_set


def one_file_one_field(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i) + fd.FLD),)

    return value_set


def one_field_ordered(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i) + fd.FLD),)

    return value_set


def two_field_one_ordered(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        for i in range(default_records):
            yield ((fld, str(i) + fd.FLD), (fldord, str(i) + fd.FLDORD),)

    return value_set


def two_field_one_invisible(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        for i in range(default_records):
            yield ((fld, str(i) + fd.FLD), (fldinv, str(i) + fd.FLDINV),)

    return value_set


def three_field_one_invisible(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        for i in range(default_records):
            yield (
                (fld, str(i) + fd.FLD),
                (fldord, str(i) + fd.FLDORD),
                (fldinv, str(i) + fd.FLDINV),
            )

    return value_set


def data_data_ord_inv(default_records=200):
    """Return an iterator which returns default_records empty value sets."""

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        data = fs.FileSpec.field_name(fd.DATA)
        for i in range(default_records):
            yield (
                (fld, str(i) + fd.FLD),
                (fldord, str(i) + fd.FLDORD),
                (data, str(i) + fd.DATA),
                (fldinv, str(i) + fd.FLDINV),
            )

    return value_set
