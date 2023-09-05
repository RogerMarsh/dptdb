# Compiler settings.

CXX = $(PATH_TO_CXX)$(COMPILER)
DEFOPTS = $(DEFINES) $(OPTIONS)
CXXEXTRA = -D_BBDBAPI
DPT_LDFLAGS = -shared

# Build includes (-I) options for compiler.

V3R0_INCLUDE = -I$(V3R0_INC) -I$(V3R0_STDAFX)
V3R0API_INCLUDE = -I$(V3R0_INC) -I$(V3R0API_INC) -I$(V3R0_STDAFX)
DPTAFX_INCLUDE = -I$(V3R0_INC) -I$(V3R0_STDAFX)

# Pattern rules DPT C++.

$(V3R0_OBJECT)/%.o : $(V3R0_SRC)/%.cpp
	$(WINE) $(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(V3R0_INCLUDE) $(DEFOPTS) -o $@ $<

$(V3R0API_OBJECT)/%.o : $(V3R0API_SRC)/%.cpp
	$(WINE) $(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(V3R0API_INCLUDE) $(DEFOPTS) -o $@ $<

$(V3R0STDAFX_OBJECT)/%.o : $(V3R0_STDAFX)/%.cpp
	$(WINE) $(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(DPTAFX_INCLUDE) $(DEFOPTS) -o $@ $<

# Object file names.

OBJS = $(SED_NAMES:%=$(V3R0_OBJECT)/%.o)

API_OBJS = $(SEDAPI_NAMES:%=$(V3R0API_OBJECT)/%.o)

AFX_OBJS = $(SEDAFX_NAMES:%=$(V3R0STDAFX_OBJECT)/%.o)

OBJECT_FILES = $(OBJS) $(AFX_OBJS) $(API_OBJS)

$(OBJECT_FILES) : $(V3R0_STDAFX)/stdafx.h $(INCS) $(API_INCS)

# Object directories.

$(V3R0_OBJECT) : $(V3R0)
	-mkdir $(V3R0_OBJECT)

$(V3R0STDAFX_OBJECT) : $(V3R0_OBJECT)
	-mkdir $(V3R0STDAFX_OBJECT)

$(V3R0API_OBJECT) : $(V3R0_OBJECT)
	-mkdir $(V3R0API_OBJECT)

$(V3R0SWIG_OBJECT) : $(V3R0_OBJECT)
	-mkdir $(V3R0SWIG_OBJECT)

OBJECT_DIRECTORIES = $(V3R0STDAFX_OBJECT) $(V3R0API_OBJECT)

# Copy package template directory for build and local install.

$(V3R0_PACKAGE) : package-template
	-mkdir $@
	cp -rp $</* $@/

# SWIG wrapper rules.
# Comments on 'sed' edits for the MinGW (sourceforge.net/projects/mingw),
# not MinGW-w64 (mingw-w64.org), toolchain are removed compared with the
# replaced dptMakefile.
# sourceforge.net/projects/mingw refers to osdn.net/projects/mingw which
# does not exist at 2023-08-09, and mingw-w64.org distinguishes itself from
# mingw.org, an earlier home for sourceforge.net/projects/mingw I believe.
# See dptdb versions earlier than 0.9 if it seems they might be relevant.

# There is a clash between MinGW and Python on _hypot and hypot for cmath.
# www.freelists.org/post/nuitka-dev/error-hypot-has-not-been-declared,2 and
# stackoverflow.com/questions/10660524/error-building-boost-...-gcc-4-7-0...
# are two of many threads suggesting two possible workarounds.  (Why is
# this project not affected until after MinGW-5.3.0 given Boost's 4.7.0
# experience?) -D_hypot=hypot added to Swig wrapper build.

# At 2023-08-09 the swig workaround for hypot clash was seen in generated
# dptapi_python_wrap.cxx so the -D_hypot=hypot is removed.

PYTHON_NAME = python
SWIG_PYTHON = $(PYTHON_NAME)
PYTHON_MAJOR_MINOR ?= 3.10
PYTHON_VERSION = $(PYTHON_MAJOR_MINOR)

# Library is python3.10 and header is python3.10 for version 3.10 of Python.
# This is different naming than for Microsoft Windows Python.
# SYSTEM_LIBRARY is assumed equivalent to PYTHON_LIBS_DIRECTORY)\python3.lib
# in the 'v3r0_vs_build.Nmk' version of this makefile in it's effect on the
# outcome.
# The printenv command at a 'Msys2 mingw32' terminal gives MSYSTEM_PREFIX
# as '/mingw32', but 'os.environ' in a Python session at this terminal
# gives MSYSTEM_PREFIX as 'C:/msys64/mingw32'.  The 'C:/msys64' is assumed
# to be a reference to the Msys64 installation directory (the default in
# this case).  It is assumed a mistake to give the 'C:/msys64' in the '-L'
# argument of the action for the rule to make the '.pyd' file.
# PYTHON_INCLUDE, not PYTHON_INCLUDE_DIRECTORY like in v3r0_vs_build.Nmk,
# as an '-I' argument for the WRAP_O target's action.
# AFX_OBJS could be removed from the '.pyd' file rule because it does not
# cause stdafx.o to be included in the dptMakefile for versions of dptdb
# earlier than 1.0 without apparent bad effects.  It looks like a problem
# to be fixed in dptMakefile and do the same here.

PYTHON_HEADER = $(PYTHON_NAME)$(PYTHON_VERSION)
PYTHON_VERSION_DIRECTORY = $(MSYSTEM_PREFIX)
PYTHON_INCLUDE_DIRECTORY = $(PYTHON_VERSION_DIRECTORY)/include
PYTHON_INCLUDE = $(PYTHON_INCLUDE_DIRECTORY)/$(PYTHON_HEADER)
PYTHON_LIBRARY = $(SWIG_PYTHON)$(PYTHON_VERSION)
SYSTEM_LIBRARY = $(MSYSTEM_PREFIX)/bin

WRAP_CXX = $(V3R0_SWIG)/$(SWIG_DPTAPI)_$(SWIG_PYTHON)_wrap.cxx
WRAP_O = $(V3R0SWIG_OBJECT)/$(SWIG_DPTAPI)_$(SWIG_PYTHON)_wrap.o

$(WRAP_CXX) : $(V3R0_PACKAGE) $(V3R0_SWIG)/$(SWIG_INTERFACE)
	swig -c++ -$(SWIG_PYTHON) -o $@ -outdir $(V3R0_PACKAGE_DPTDB) -I$(V3R0API_INC) $(V3R0_SWIG)/$(SWIG_INTERFACE)

$(WRAP_O) : $(V3R0SWIG_OBJECT) $(WRAP_CXX)
	$(WINE) $(CXX) -c $(CXXEXTRA) $(CXXFLAGS) -I$(V3R0API_INC) -I$(V3R0_INC) -I$(PYTHON_INCLUDE) $(DEFOPTS) -o $@ $(WRAP_CXX)

# The .pyd file built from SWIG.

$(V3R0_PACKAGE_DPTDB)/$(PYTHON_API_DLL) : $(OBJECT_DIRECTORIES) $(OBJECT_FILES) $(WRAP_O)
	$(WINE) $(CXX) $(DPT_LDFLAGS) -o $@ $(WRAP_O) $(API_OBJS) $(OBJS) -l$(PYTHON_LIBRARY) -L$(SYSTEM_LIBRARY)

wrapper : $(V3R0_PACKAGE_DPTDB)/$(PYTHON_API_DLL)
	python -m build --wheel --no-isolation $(V3R0_PACKAGE)

local-install : wrapper
	python -m pip install --user --no-index --find-links $(V3R0_PACKAGE)/dist dpt3.0_dptdb
