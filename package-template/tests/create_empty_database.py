# create_empty_database.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Create empty databases defined in file_definitions module."""
import os
    
import dpt_database


def create_empty_database(name, definition, directory=None):
    """Create and return database with definition in directory/name."""
    if directory is None:
        directory = dpt_database.directory_with_bitness()
    directory = os.path.join(directory, name)
    database = dpt_database.DPTDatabase(directory, filedefs=definition)
    database.create()
    return database
