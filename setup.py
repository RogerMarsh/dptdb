# setup.py
# Copyright 2013 Roger Marsh
# Licence: See LICENCE (BSD licence)
"""DPT API setup script
"""
# There is a Makefile in the DPT distribuion file with multi-language support
# in mind.
#
# This script works directly on the zipped DPT distribution file.
#
# The attempt to use the Mingw32CCompiler class fails in three ways.
# C++ #include statements refer to stdafx.h but the file name is StdAfx.h
# On fixing this by renaming the file, the first few *.cpp files compile but
# bmset.cpp fails at line 53 of du1step.h "error: forward declaration of 'const
# struct dpt::DU1FieldIndex'".  Eight other files fail to compile for the same
# reason.
# It is not clear how to persuade build_ext to use the mingw toolset to do the
# SWIG part of the build.  The nine compilation failures were ignored while
# trying to do this.
#
# No difference attempting to force the command to look like the one used in
# dptMakefile by calls to set_executables().
#
# This setup script does the C++ part of the build by driving the make in
# dptMakefile (the nine modules above are compiled successfully here) and then
# completes the package build using distutils.core.setup.

import os
import sys
import subprocess
import zipfile
import shutil
import distutils.core
import distutils.command

# Used to check a previously extracted version is the one being extracted.
_EXTRACT = 'dptextract'

# Edits to _EXTRACT required for successful build in environment with the
# version of mingw32-g++ used.
_BUILD = 'dptbuild'


def setup(
    dpt_distribution_file='DPT_V3R0_DBMS.ZIP',
    path_to_swig='C:/swigwin-2.0.8',
    swig_command='swig2.0',
    assume_gcc_3_4_5='true',
    **attrs):
    """Extract DPT source code from distribution and call distutils.setup

    dpt_distribution_file is the default for DPT_DIST=filename in sys.argv
    path_to_swig is the default for PATH_TO_SWIG=directoryname in sys.argv
    swig_command is the default for SWIG_COMMAND=programname in sys.argv
    assume_gcc_3_4_5 is the default for ASSUME_GCC_3_4_5=flag in sys.argv

    PATH_TO_SWIG and path_to_swig are ignored when cross-compiling under *nix.

    SWIG_COMMAND and swig_command are ignored under Microsoft Windows and Wine.

    gcc-3.4.5 is the most recent version supported by MinGW known to compile
    the DPT API in dpt_distribution_file on Microsoft Windows or Wine without
    any modifications.  If True assume mingw32-g++ version 3.4.5 is available
    and do not do the changes needed to allow a successful build under later
    versions.

    When cross-compiling on *nix some changes from '#include "dir\file.h' to
    '#include "dir/file.h' are needed whatever version is available.

    """
    
    if sys.platform == 'win32':
        # The problem here is finding a reliable test to distinguish running
        # under Wine from running under Microsoft Windows.
        if os.getenv('OSTYPE') != 'msys':
            # Maybe do not try and print this message as helpful advice.
            #sys.stdout.write(
            #    'On Microsoft Windows this setup must be run in an MSYS shell')
            pass#return
    
    if len(sys.argv) < 2:
        sys.stdout.write('Please specify a distutils command to setup.py')
        return
    
    if sys.argv[1] not in distutils.command.__all__:
        sys.stdout.write(' '.join((sys.argv[1], 'is not a distutils command')))
        return
    
    for a in sys.argv[2:]:
        if a.startswith('DPT_DIST='):
            dpt_distribution_file = a.split('=')[-1].strip()
    
    for a in sys.argv[2:]:
        if a.startswith('PATH_TO_SWIG='):
            path_to_swig = a.split('=')[-1].strip()
    
    for a in sys.argv[2:]:
        if a.startswith('SWIG_COMMAND='):
            swig_command = a.split('=')[-1].strip()
    
    for a in sys.argv[2:]:
        if a.startswith('ASSUME_GCC_3_4_5='):
            assume_gcc_3_4_5 = a.split('=')[-1].strip()

    distfile = os.path.join(dpt_distribution_file)
    if not os.path.exists(distfile):
        sys.stdout.write(''.join(('setup cannot find ', distfile, '\n')))
        return
    if not zipfile.is_zipfile(distfile):
        sys.stdout.write(' '.join((distfile, 'is not a zipped file\n')))
        return
    zf = zipfile.ZipFile(distfile)
    ok = False
    try:
        zipbase = os.path.join(_EXTRACT, 'zipcompare')
        present = False
        absent = False
        matched = True
        for n in zf.namelist():
            if os.path.exists(os.path.join(_EXTRACT, n)):
                if os.path.isfile(os.path.join(_EXTRACT, n)):
                    present = True
                    f = open(os.path.join(_EXTRACT, n), 'rb')
                    # 'rb' is not needed on MS Windows Python 3.3.0
                    # 'rb' is needed on Python 3.3.0 built from Python sources
                    # on FreeBSD.
                    # Not known what the FreeBSD port of Python 3.3.n does.
                    # This port is available now, so will find out shortly.
                    try:
                        pft = f.read()
                    finally:
                        f.close()
                    zf.extract(n, path=zipbase)
                    f = open(os.path.join(zipbase, n), 'rb')
                    try:
                        eft = f.read()
                    finally:
                        f.close()
                    del f
                    if eft != pft:
                        sys.stdout.write(' '.join(('file', n, 'changed\n')))
                        matched = False
            else:
                absent = True
            if n == 'licence.txt':
                if os.path.exists(os.path.join(n)):
                    if os.path.isfile(os.path.join(n)):
                        present = True
                        f = open(os.path.join(n), 'rb')
                        try:
                            pft = f.read()
                        finally:
                            f.close()
                        f = open(os.path.join(zipbase, n), 'rb')
                        try:
                            eft = f.read()
                        finally:
                            f.close()
                        del f
                        if eft != pft:
                            sys.stdout.write(' '.join(('file', n, 'changed\n')))
                            matched = False
                else:
                    absent = True
        if present and absent:
            # error
            pass # ok initialised False
        elif absent:
            # extract files
            zf.extractall(path=_EXTRACT)
            zf.extract('licence.txt') # for ease of redistribution
            ok = True
        elif present:
            ok = matched # all existing files must be unchanged
        if present:
            shutil.rmtree(zipbase)
    finally:
        zf.close()
    if not ok:
        sys.stdout.write(
            ' '.join(('setup abandonned because existing extracted',
                      'files do not match zipped distribution file.\n')))
        return
    
    builddir = os.path.join(os.getcwd(), _BUILD)
    for bd in (
        builddir,
        os.path.join(builddir, 'stdafx'),
        os.path.join(builddir, 'source'),
        os.path.join(builddir, 'include'),
        os.path.join(builddir, 'source', 'dbapi'),
        os.path.join(builddir, 'include', 'dbapi'),
        ):
        try:
            os.mkdir(bd)
        except:
            if not os.path.isdir(bd):
                sys.stdout.write('Create build directory fails\n')
                return
    stdafx_copy = (
        # C++ #include statements refer to stdafx.h
        (os.path.join(
            _EXTRACT, 'sample projects', 'HelloWorld! (MSVC)', 'StdAfx.h'),
         os.path.join(_EXTRACT, 'stdafx', 'stdafx.h')),
        # dptMakefile refers to stdafx.cpp and directory names are awkward
        (os.path.join(
            _EXTRACT, 'sample projects', 'HelloWorld! (MSVC)', 'StdAfx.cpp'),
         os.path.join(_EXTRACT, 'stdafx', 'stdafx.cpp')),
        # dptMakefile refers to dptapi_python.i and directory names are awkward
        (os.path.join(
            _EXTRACT, 'sample projects', 'DPT with Python', 'dptapi_python.i'),
         os.path.join(_BUILD, 'dptapi_python.i')),
        )
    for inp, outp in stdafx_copy:
        if os.path.isfile(outp):
            f = open(inp)
            try:
                pft = f.read()
            finally:
                f.close()
            f = open(outp)
            try:
                eft = f.read()
            finally:
                f.close()
            del f
            if eft != pft:
                ok = False
        else:
            f = open(inp)
            try:
                pft = f.read()
                if len(os.path.dirname(outp)):
                    try:
                        os.makedirs(os.path.dirname(outp))#, exist_ok=True)
                    except OSError:
                        pass # assume target directory already exists
                fo = open(outp, 'w')
                try:
                    fo.write(pft)
                finally:
                    fo.close()
                del fo
            finally:
                f.close()
            del f


    def get_source_files(directory):
        """Return list of *.cpp source files without extention.""" 
        files =[]
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, f)):
                p, e = os.path.splitext(f)
                if e in ('.cpp',):
                    files.append(p)
        return files


    def get_include_files(directory):
        """Return list of *.h source files without extention.""" 
        files =[]
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, f)):
                p, e = os.path.splitext(f)
                if e in ('.h',):
                    files.append(p)
        return files


    # GNU make is called gmake in *nix systems but make in msys.
    if sys.platform != 'win32':
        command = 'gmake'
    else:
        command = 'make'

    for exdir in (
        'stdafx',
        'source',
        'include',
        os.path.join('source', 'dbapi'),
        os.path.join('include', 'dbapi'),
        ):
        pass

    job = [
        command,
        '-f',
        '/'.join(os.path.join(
            '..', 'dptMakefile').split('\\')),
        'python']

    job.append(
        ''.join(
            ('DPT_NAMES=',
             ' '.join(get_source_files(
                 os.path.join(_EXTRACT, 'source'))),
             )))
    job.append(
        ''.join(
            ('DPTAPI_NAMES=',
             ' '.join(get_source_files(
                 os.path.join(_EXTRACT, 'source', 'dbapi'))),
             )))

    job.append(
        ''.join(
            ('DPT_INC_NAMES=',
             ' '.join(get_include_files(
                 os.path.join(_EXTRACT, 'include'))),
             )))
    job.append(
        ''.join(
            ('DPTAPI_INC_NAMES=',
             ' '.join(get_include_files(
                 os.path.join(_EXTRACT, 'include', 'dbapi'))),
             )))
    job.append(''.join(('OPTIONS=', '-O3')))
    job.append(''.join(('DEFINES=', '-DNDEBUG')))
    
    if assume_gcc_3_4_5 != 'true':
        job.append(''.join(('GCC_VERSION_PATCHING=', 'false')))
    if sys.platform == 'win32':
        job.append(''.join(('PATH_TO_SWIG=', path_to_swig)))
    else:
        job.append(''.join(('SWIG_COMMAND=', swig_command)))
        if assume_gcc_3_4_5 == 'true':
            job.append(''.join(('GCC_VERSION_PATCHING=', 'nixtrue')))
        else:
            job.append(''.join(('GCC_VERSION_PATCHING=', 'nixfalse')))

    path_to_python = None
    for a in sys.argv[2:]:
        if a.startswith('PATH_TO_PYTHON='):
            path_to_python = a
    if path_to_python:
        job.append(path_to_python)
    python_version = None
    for a in sys.argv[2:]:
        if a.startswith('PYTHON_VERSION='):
            python_version = a
    if python_version:
        job.append(python_version)

    job.append(''.join(('PYTHON_RUNNING_MAKE=', sys.executable)))

    # Use make -f dptMakefile ... for non-default C++ build of DPT API.
    # Arguments dpt_distribution_file and path_to_swig allow some flexibility
    # using setup.
    sp = subprocess.Popen(job, cwd=builddir)
    
    r = sp.wait()
    if r != 0:
        sys.stdout.write('Build C++ extension module fails\n')
        return

    version = release = major = minor = '0'
    version_file = os.path.join('..', 'version.py')
    for nv in open(os.path.join('version.py')):
        nv = [v.strip() for v in nv.split('=')]
        if len(nv) == 2:
            n, v = nv
            if n == '_dpt_version':
                v = v[1:-1].split('.')
                if len(v) == 2:
                    version, release = v
            elif n == '_dptdb_version':
                v = v[1:-1].split('.')
                if len(v) == 2:
                    major, minor = v

    # Default should be same as PYTHON_VERSION in dptMakefile
    if python_version is None:
        python_version = '33'
    else:
        python_version = python_version.split('=')[-1]
    if sys.argv[1] == 'sdist':
        name = '.'.join(
            ('dptdb',
             ''.join(('dpt', version, '.', release)),
             ))
    else:
        name = '.'.join(
            ('dptdb',
             ''.join(
                 ('py',
                  '.'.join(
                      tuple(python_version)),
                  )),
             ''.join(('dpt', version, '.', release)),
             ))

    # Remove all non-distutils commands from sys.argv before setup() call
    # The first two must be valid for setup() to work.  Let setup complain if
    # anything is wrong there.
    argv = sys.argv[:]
    for e in range(len(sys.argv)-1, 1, -1):
        if sys.argv[e] not in distutils.command.__all__:
            del sys.argv[e]
    distutils.core.setup(name=name, version='.'.join((major, minor)), **attrs)
    sys.argv[:] = argv


if __name__ == '__main__':
    setup(
        description='SWIG interface to DPT for Python',
        author='solentware.co.uk',
        author_email='roger.marsh@solentware.co.uk',
        url='http://www.solentware.co.uk',
        package_dir={'dptdb':''},
        packages=[
            'dptdb',
            ],
        platforms='Microsoft Windows',
        package_data={
            '': ['_dptapi.pyd',
                 'licence.txt',
                 'LICENCE'
                 ],
            },
        long_description='''SWIG interface to DPT for Python

        Built from the DPT API source code available at

        www.dptoolkit.com
        ''',
        )
