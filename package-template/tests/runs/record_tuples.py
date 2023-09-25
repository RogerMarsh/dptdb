# record_tuples.py
# Copyright 2023 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Define iterators record value sets for tests."""
import filespec as fs
import file_definitions as fd


def one_file_no_fields(default_records=200, modulus=None):
    """Return iterator yielding one_file_no_fields value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        for i in range(default_records):
            yield ()

    return value_set


def one_file_one_field(default_records=200, modulus=None):
    """Return iterator yielding one_file_one_field value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i % modulus) + fd.FLD),)

    return value_set


def one_field_ordered(default_records=200, modulus=None):
    """Return iterator yielding one_field_ordered value sets."""
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        for i in range(default_records):
            yield ((fld, str(i % modulus) + fd.FLD),)

    return value_set


def two_field_one_ordered(default_records=200, modulus=None):
    """Return iterator yielding two_field_one_ordered value sets."""
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
    """Return iterator yielding two_field_one_invisible value sets."""
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
    """Return iterator yielding three_field_one_invisible value sets."""
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
    """Return iterator yielding data_data_ord_inv value sets."""
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


def data_data_ord_inv_upper(default_records=200, modulus=None):
    """Return iterator yielding data_data_ord_inv value sets.

    The field names are forced to upper case.  Used to demonstrate
    fastload is incompatible with non-uppercase field names like
    'Fieldname' for example.

    """
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD).upper()
        fldord = fs.FileSpec.field_name(fd.FLDORD).upper()
        fldinv = fs.FileSpec.field_name(fd.FLDINV).upper()
        data = fs.FileSpec.field_name(fd.DATA).upper()
        for i in range(default_records):
            j = i % modulus
            yield (
                (fld, str(j) + fd.FLD),
                (fldord, str(j) + fd.FLDORD),
                (data, str(j) + fd.DATA),
                (fldinv, str(j) + fd.FLDINV),
            )

    return value_set


def vis_inv_inv_inv(default_records=200, modulus=None):
    """Return iterator yielding vis_inv_inv_inv value sets.

    Keep the field names for other iterators, but the vis_inv_inv_inv
    file_definitions entry defines fldord, fldinv and data as INV.

    A suitable choice of modulus causes a few index values to get bitmap
    representation of inverted list of record numbers, while most get
    the list representation.

    The number of index values per record causes the update to be done
    in multiple chunks, as reported in audit.txt generated by the DPT
    code,

    """
    if modulus is None:
        modulus = default_records

    def value_set():
        fld = fs.FileSpec.field_name(fd.FLD)
        fldord = fs.FileSpec.field_name(fd.FLDORD)
        fldinv = fs.FileSpec.field_name(fd.FLDINV)
        data = fs.FileSpec.field_name(fd.DATA)
        for i in range(default_records):
            j10th = i % modulus
            j = i % (modulus * 10)
            yield tuple(
                [(fld, str(i) + fd.FLD)] +
                [(fldord, str(j10th) + fd.FLDORD)] +
                [(fldord, str(j) + fd.FLDORD + str(k)) for k in range(1000)] +
                [(data, str(i) + fd.DATA + str(k)) for k in range(1050)] +
                [(fldinv, str(i) + fd.FLDINV + str(k)) for k in range(1100)]
            )

    return value_set


all_record_generators = (
    (
        fd.ONE_FILE_NO_FIELDS,
        fd.one_file_no_fields,
        one_file_no_fields,
    ),
    (
        fd.ONE_FILE_ONE_FIELD,
        fd.one_file_one_field,
        one_file_one_field,
    ),
    (
        fd.ONE_FIELD_ORDERED,
        fd.one_field_ordered,
        one_field_ordered,
    ),
    (
        fd.TWO_FIELD_ONE_ORDERED,
        fd.two_field_one_ordered,
        two_field_one_ordered,
    ),
    (
        fd.TWO_FIELD_ONE_INVISIBLE,
        fd.two_field_one_invisible,
        two_field_one_invisible,
    ),
    (
        fd.THREE_FIELD_ONE_INVISIBLE,
        fd.three_field_one_invisible,
        three_field_one_invisible,
    ),
    (
        fd.DATA_DATA_ORD_INV,
        fd.data_data_ord_inv,
        data_data_ord_inv,
    ),
)

record_generators = all_record_generators[2:]
