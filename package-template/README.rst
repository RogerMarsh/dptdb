==========================================
DPT database API wrappers built using SWIG
==========================================

.. contents::


Description
===========

This package provides Python applications with the database API used by DPT.

DPT is a multi-user database system for Microsoft Windows.

The Python application can be as simple as a single-threaded process embedding the DPT API.

These are links to DPT `source`_ and `documentation`_ zip files, and both files are available at `Github.com/RogerMarsh/dptdb`_ too.  

There is no separate documentation for Python.


Installation Instructions
=========================


Install the package by typing

   'py -m pip install --user dpt3.0_dptdb'

in Windows PowerShell.


Sample code
===========

The dpt3.0_dptdb/test directory contains a simple application which populates a database, using some contrived data, and does some simple data retrievals.

This can be run on Microsoft Windows by typing

   'py pydpt-test.py'

in Windows PowerShell with dpt3.0_dptdb/test as the current directory.


The sample application offers seven options which create databases with different numbers of records.  Each record has 6 fields and all fields are indexed.

   One option, called normal, adds 246,625 records to a database in a 16 Mb file in about 3.33 minutes with transaction backout enabled.

   The shortest option adds 246,625 records to a database in a 16 Mb file in about 0.6 minutes with transaction backout disabled.

   The longest option adds 7,892,000 records to a database in a 526 Mb file in about 18.75 minutes with transaction backout disabled.

The figures are for a 2Gb 667MHz memory, 1.8GHz CPU, solid state drive, Microsoft Windows XP installation.


Restrictions
============

This package does not run in a `Msys2`_ environment under Microsoft Windows, but the dptdb builder can be downloaded and used to build and install dptdb in that environment.

It is not known if dptdb is now usable in a `Msys2`_ environment under `Wine`_, or if the restrictions which affected the old versions built in a `MinGW`_ environment would be relevant.


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
