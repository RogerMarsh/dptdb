# file_definitions.py
# Copyright 2023 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Define sample FileSpec instances for tests."""
import filespec as fs 

ONE_FILE_NO_FIELDS = "nofields"
one_file_no_fields = {
    ONE_FILE_NO_FIELDS : {
        fs.DDNAME: fs.FileSpec.dpt_dd(ONE_FILE_NO_FIELDS),
        fs.FILE: fs.FileSpec.dpt_dsn(ONE_FILE_NO_FIELDS),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {},
    },
}

ONE_FILE_ONE_FIELD = "onefield"
one_file_one_field = {
    ONE_FILE_ONE_FIELD : {
        fs.DDNAME: fs.FileSpec.dpt_dd(ONE_FILE_ONE_FIELD),
        fs.FILE: fs.FileSpec.dpt_dsn(ONE_FILE_ONE_FIELD),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): None,
        },
    },
}

ONE_FIELD_ORDERED = "oneford"
one_field_ordered = {
    ONE_FIELD_ORDERED : {
        fs.DDNAME: fs.FileSpec.dpt_dd(ONE_FIELD_ORDERED),
        fs.FILE: fs.FileSpec.dpt_dsn(ONE_FIELD_ORDERED),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): {fs.ORD: True},
        },
    },
}

TWO_FIELD_ONE_ORDERED = "twoford"
two_field_one_ordered = {
    TWO_FIELD_ONE_ORDERED : {
        fs.DDNAME: fs.FileSpec.dpt_dd(TWO_FIELD_ONE_ORDERED),
        fs.FILE: fs.FileSpec.dpt_dsn(TWO_FIELD_ONE_ORDERED),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): None,
            fs.FileSpec.field_name("fldord"): {fs.ORD: True},
        },
    },
}

TWO_FIELD_ONE_INVISIBLE = "twofinv"
two_field_one_invisible = {
    TWO_FIELD_ONE_INVISIBLE : {
        fs.DDNAME: fs.FileSpec.dpt_dd(TWO_FIELD_ONE_INVISIBLE),
        fs.FILE: fs.FileSpec.dpt_dsn(TWO_FIELD_ONE_INVISIBLE),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): None,
            fs.FileSpec.field_name("fldinv"): {fs.ORD: True, fs.INV: True},
        },
    },
}

THREE_FIELD_ONE_INVISIBLE = "ordfinv"
three_field_one_invisible = {
    THREE_FIELD_ONE_INVISIBLE : {
        fs.DDNAME: fs.FileSpec.dpt_dd(THREE_FIELD_ONE_INVISIBLE),
        fs.FILE: fs.FileSpec.dpt_dsn(THREE_FIELD_ONE_INVISIBLE),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): None,
            fs.FileSpec.field_name("fldord"): {fs.ORD: True},
            fs.FileSpec.field_name("fldinv"): {fs.ORD: True, fs.INV: True},
        },
    },
}

DATA_DATA_ORD_INV = "ddoiflds"
data_data_ord_inv = {
    DATA_DATA_ORD_INV : {
        fs.DDNAME: fs.FileSpec.dpt_dd(DATA_DATA_ORD_INV),
        fs.FILE: fs.FileSpec.dpt_dsn(DATA_DATA_ORD_INV),
        fs.FILEDESC: {
            fs.BRECPPG: 10,
            fs.FILEORG: fs.RRN,
        },
        fs.BTOD_FACTOR: 1,
        fs.BTOD_CONSTANT: 30,
        fs.DEFAULT_RECORDS: 200,
        fs.FIELDS: {
            fs.FileSpec.field_name("fld"): None,
            fs.FileSpec.field_name("fldord"): {fs.ORD: True},
            fs.FileSpec.field_name("fldinv"): {fs.ORD: True, fs.INV: True},
            fs.FileSpec.field_name("data"): None,
        },
    },
}
