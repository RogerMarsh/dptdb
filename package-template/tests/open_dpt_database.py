# open_dpt_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Open DPT databases defined in file_definitions module."""
import os
    
import dpt_database


def open_dpt_database(name, definition, directory=None):
    """Return database for definition in directory/name.

    The database is created if it does not exist.

    An OpenContext for each database file is available in self.contexts
    dict keyed by a file name from the file_definitions module used in
    the file_definition function which defines the database.

    """
    if directory is None:
        directory = dpt_database.directory_with_bitness()
    directory = os.path.join(directory, name)
    database = dpt_database.DPTDatabase(directory, filedefs=definition)
    database.create()
    return database
