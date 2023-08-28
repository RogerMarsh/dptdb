# record_tuples.py
# Copyright 2023 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Define sample FileSpec instances for tests."""
import filespec as fs
import file_definitions as fd


def one_file_no_fields(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        for i in range(default_records):
            yield ()

    return value_set


def one_file_one_field(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i % modulus) + fd.FLD),)

    return value_set


def one_field_ordered(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i % modulus) + fd.FLD),)

    return value_set


def two_field_one_ordered(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        for i in range(default_records):
            j = i % modulus
            yield ((fld, str(j) + fd.FLD), (fldord, str(j) + fd.FLDORD),)

    return value_set


def two_field_one_invisible(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        for i in range(default_records):
            j = i % modulus
            yield ((fld, str(j) + fd.FLD), (fldinv, str(j) + fd.FLDINV),)

    return value_set


def three_field_one_invisible(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        for i in range(default_records):
            j = i % modulus
            yield (
                (fld, str(j) + fd.FLD),
                (fldord, str(j) + fd.FLDORD),
                (fldinv, str(j) + fd.FLDINV),
            )

    return value_set


def data_data_ord_inv(default_records=200, modulus=None):
    """Return an iterator which returns default_records empty value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        data = fs.FileSpec.field_name(fd.DATA)
        for i in range(default_records):
            j = i % modulus
            yield (
                (fld, str(j) + fd.FLD),
                (fldord, str(j) + fd.FLDORD),
                (data, str(j) + fd.DATA),
                (fldinv, str(j) + fd.FLDINV),
            )

    return value_set
