==========================================
DPT database API wrappers built using SWIG
==========================================

.. contents::


Description
===========

This package provides Python applications with the database API used by DPT.

DPT is a multi-user database system for Microsoft Windows.

This package contains two modules: a Python interface to the DPT API built using `SWIG`_ and multistep_sort which is an implementation of the sorts needed by DPT's multi-step deferred update process for efficient updates.

These are links to DPT `source`_ and `documentation`_ zip files, and both files are available at `Github.com/RogerMarsh/dptdb`_ too.  

There is no separate documentation for Python.

There are no source distributions (*.tar.gz files), only wheels.  For source see `Github.com/RogerMarsh/dptdb`_ which builds the wheels.


Installation Instructions
=========================


Install the package by typing

   'py -m pip install --user dpt3.0_dptdb'

in Windows PowerShell (see 'py' documentation for selecting Python version),

or

   'python -m pip install --user dpt3.0_dptdb'

in a Msys2 MINGW32 or Msys2 MINGW64 shell.


32-bit Builds
=============

32-bit builds on `MinGW`_ (mingw.org and replacements which no longer exist) produced runnable packages until Python 3.7, and dpt3.0-dptdb was ignored after that until the Developer Command Prompt for Visual Studio products were noticed.

The dpt3.0_dptdb/tests/runs/pydpt-test.py module, which populates a database with some contrived data in an attempt to demonstrate running out of memory when run under `Wine`_, is retained from mingw.org days.

32-bit builds on `Msys2`_ and Developer Command Prompt for VS2017 are runnable on Python 3.8 and later (and probably wherever the old mingw.org-based builds would run).


64-bit Builds
=============

64-bit builds on `Msys2`_ and Developer Command Prompt for VS2017 are runnable after avoiding a few problems located with some test runs.

The dpt3.0_dptdb/tests/runs directory contains a number of test runs devised to determine where single-step deferred update fails on 64-bit Python builds.  These are the run_test_inverted_* modules.  Note single-step deferred update does work in a few cases on 64-bit Python builds assuming the single-step interface is not suppressed.

The dpt3.0_dptdb/tests/runs directory contains a number of test runs devised to verify the operation of multi-step deferred update on 64-bit Python builds using the multistep_sort module installed alongside dptapi in dptdb.  These are the run_test_multistep_* modules.

The dpt3.0_dptdb/tests/runs directory contains a number of test runs devised to determine where traversal of database in index order fails on 64-bit Python builds.  These are the run_test_traverse_* modules.


32-bit and 64-bit Builds
========================

The dpt3.0_dptdb/tests/runs directory contains a number of test runs devised to verify the operation of file reorganization runs with and without the patch to prevent renaming fields to all upper-case.  These are the run_test_reorganize_* modules.


Restrictions
============

The DPT API OpenContext_DUSingle interface is suppressed in 64-bit builds because this style of deferred update (DU) does not work in these environments.

The obsolescent OpenContextDUMulti interface has to be used to do deferred updates in 64-bit environments.

The multistep_sort module is added alongside the dptapi module built by SWIG to support OpenContextDUMulti as a consequence of the suppression of OpenContext_DUSingle.


Notes
=====

This package is built from `DPT_V3R0_DBMS.ZIP`_, a recent DPT API source code distribution, by default.

You will need the `DPT API documentation`_ to use this package.  This is included as `DBAPI.html`_ in DPT_V3R0_DOCS.ZIP.

The `DPT API distribution`_ contains independent scripts and instructions to build dptdb mentioning much earlier versions of the build dependencies.


.. _DPT API documentation: http://solentware.co.uk/files/DPT_V3R0_DOCS.ZIP
.. _documentation: http://solentware.co.uk/files/DPT_V3R0_DOCS.ZIP
.. _DBAPI.html: http://solentware.co.uk/files/DPT_V3R0_DOCS.ZIP
.. _relnotes_V2RX.html: http://solentware.co.uk/files/DPT_V3R0_DOCS.ZIP
.. _DPT_V3R0_DBMS.ZIP: http://solentware.co.uk/files/DPT_V3R0_DBMS.ZIP
.. _DPT API distribution: http://solentware.co.uk/files/DPT_V3R0_DBMS.ZIP
.. _source: http://solentware.co.uk/files/DPT_V3R0_DBMS.ZIP
.. _Msys2: http://msys2.org
.. _Python: https://python.org
.. _SWIG: http://swig.org
.. _MinGW: http://mingw.org
.. _Wine: https://winehq.org
.. _Github.com/RogerMarsh/dptdb : https://github.com/RogerMarsh/dptdb
