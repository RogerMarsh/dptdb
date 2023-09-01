# add_records.py
# Copyright 2023 Roger Marsh
# License: BSD license

"""Add records to databases.

The commit, backout, txn_per_record and deferred arguments control the
environment of the add records run.

deferred: True - index updates are deferred and transactions are disabled.
                commit, backout, and txn_per_record are ignored.
txn_per_record: True - each record is added in a separate transaction.
commit: True - transactions are explicitly committed.
                If commit is False a record is not added in a separate
                transaction.
backout: True - transactions are explicitly backed out.
                Default is False.
                If backout is False a record is not added, and then backed
                out, in a separate transaction.

If commit and backout are both False the default action, by default commit,
occurs when the database is closed.

"""
import os
    
import dpt_database


def _add_records(
    name,
    definition,
    records=(),
    commit=True,
    backout=False,
    txn_per_record=True,
    deferred=False,
    directory=None,
):
    """Add records to database with definition in directory/name.

    Default is commit after every record, but allow for a single large
    transaction or deferred updates; and backout too.

    """
    if directory is None:
        directory = dpt_database.directory_with_bitness()
    directory = os.path.join(directory, name)
    database = dpt_database.DPTDatabase(
        directory, deferred=deferred, filedefs=definition
    )
    database.create()
    for record in records():
        database.add_record(database.contexts[name], record=record)
        if not deferred:
            if txn_per_record and commit:
                database.database_services.Commit()
            elif txn_per_record and backout:
                database.database_services.Backout()
    if not deferred:
        if not txn_per_record and commit:
            database.database_services.Commit()
        elif not txn_per_record and backout:
            database.database_services.Backout()
    return database


def keep_records(*args, **kwargs):
    """Delegate to _add_records then close database."""
    _add_records(*args, **kwargs).close_database()


def add_records(*args, **kwargs):
    """Delegate to _add_records then delete database."""
    _add_records(*args, **kwargs).delete()
