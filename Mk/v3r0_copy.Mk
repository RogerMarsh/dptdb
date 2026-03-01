# Build V3R0.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION
# PATH_TO_CXX
# COMPILER
# WINE
# where COMPILER is mandatory and will usually be 'cl' or 'mingw32-g++'.

# Source is downloaded by fetch.Makefile.
# V3R0, and therefore BUILD and DPT, are defined in v3r0_copy_targets and
# v3r0_mingw_targets.

DPT_LICENCE = licence.txt

# DPT extract and build folders.

V3R0_SRC = $(V3R0)/source
V3R0_INC = $(V3R0)/include
V3R0API_SRC = $(V3R0_SRC)/dbapi
V3R0API_INC = $(V3R0_INC)/dbapi
V3R0_STDAFX = $(V3R0)/stdafx
SED_SRC = $(V3R0E)/source
SED_INC = $(V3R0E)/include
SEDAPI_SRC = $(SED_SRC)/dbapi
SEDAPI_INC = $(SED_INC)/dbapi
SED_STDAFX = $(V3R0E)/stdafx

# Tests folders.

BUILD_TESTS = $(BUILD)/$(CPP_TESTS)
V3R0_TESTS = $(BUILD_TESTS)/$(DPT_VERSION)

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
V3R0_SWIG = $(V3R0)/swig
V3R0_SWIG_INTERFACE = $(V3R0_SWIG)/$(SWIG_INTERFACE)
COPY_SWIG = $(V3R0E)/$(SWIG_INTERFACE)

# Source file names.

SED_NAMES = $(basename $(notdir $(wildcard $(SED_SRC)/*.cpp)))

SEDAPI_NAMES = $(basename $(notdir $(wildcard $(SEDAPI_SRC)/*.cpp)))

SED_INC_NAMES = $(basename $(notdir $(wildcard $(SED_INC)/*.h)))

SEDAPI_INC_NAMES = $(basename $(notdir $(wildcard $(SEDAPI_INC)/*.h)))

SEDAFX_NAMES = stdafx

SRCS = $(SED_NAMES:%=$(V3R0_SRC)/%.cpp)

API_SRCS = $(SEDAPI_NAMES:%=$(V3R0API_SRC)/%.cpp)

INCS = $(SED_INC_NAMES:%=$(V3R0_INC)/%.h)

API_INCS = $(SEDAPI_INC_NAMES:%=$(V3R0API_INC)/%.h)

AFX_SRCS = $(SEDAFX_NAMES:%=$(V3R0_STDAFX)/%.cpp)

AFX_INCS = $(SEDAFX_NAMES:%=$(V3R0_STDAFX)/%.h)

SOURCE_FILES = $(SRCS) $(INCS) $(API_SRCS) $(API_INCS) $(AFX_SRCS) $(AFX_INCS)

# The build directory parent (dpt/v3r0) is created in fetch.Makefile.

$(V3R0API_SRC) : $(V3R0_SRC)
	-mkdir $(V3R0API_SRC)

$(V3R0_SRC) : $(V3R0)
	-mkdir $(V3R0_SRC)

$(V3R0API_INC) : $(V3R0_INC)
	-mkdir $(V3R0API_INC)

$(V3R0_INC) : $(V3R0)
	-mkdir $(V3R0_INC)

$(V3R0_STDAFX) : $(V3R0)
	-mkdir $(V3R0_STDAFX)

$(V3R0_SWIG) : $(V3R0)
	-mkdir $(V3R0_SWIG)

$(V3R0) : $(BUILD)
	-mkdir $(V3R0)

$(V3R0_TESTS) : $(BUILD_TESTS)
	-mkdir $(V3R0_TESTS)

$(BUILD_TESTS) : $(BUILD)
	-mkdir $(BUILD_TESTS)

$(BUILD) :
	-mkdir $(BUILD)

# Copy service initialization parameters for single step deferred update.

PARMS_DU_SINGLE = parms_dusingle.ini

$(V3R0_TESTS)/$(PARMS_DU_SINGLE) : $(CPP_TESTS)/$(PARMS_DU_SINGLE)
	cp -p $< $@

# Pattern rules for editing DPT C++.

# Normalize path element separators in #include directives as '/' for *nix
# build environment.  There are only a few files which do not comply, but do
# it always anyway for simplicity.

# MinGW-6.3.0 on Windows builds fail through use of std::make_pair where
# std::pair should be used.  Applying patch seems to leave the earlier
# MinGW-4.9.3 and MinGW-5.3.0 builds in good condition.  Problem explained
# at http://advogato.org/person/redi/diary/239.html found via
# https://stackoverflow.com/questions/32443181/stdmake-pair-with-c-11
# and there are many others (neither of these are the ones found first time).
# MinGW-6.3.0 on Windows builds give warnings in two modules that 'in c++11
# destructors default to noexcept'.  The raise exception behaviour in the two
# classes affected is retained by adding an edit to all SED_SRC and SED_INC
# files.  https://gcc.gnu.org/bugzilla/show_bug.cgi?id=56191 was sufficient
# as a hint to the edit needed.

$(V3R0_SRC)/%.cpp : $(SED_SRC)/%.cpp
	sed $(SED_SRC_EDITS) $< > $@

$(V3R0_INC)/%.h : $(SED_INC)/%.h
	sed $(SED_INC_EDITS) $< > $@

$(V3R0API_SRC)/%.cpp : $(SEDAPI_SRC)/%.cpp
	sed $(SEDAPI_SRC_EDITS) $< > $@

$(V3R0API_INC)/%.h : $(SEDAPI_INC)/%.h
	sed $(SEDAPI_INC_EDITS) $< > $@

$(V3R0_STDAFX)/%.cpp : $(SED_STDAFX)/%.cpp
	sed $(SED_STDAFX_CPP_EDITS) $< > $@

# VC6++ and MinGW-3.4.5 do not require explicit #include directives for
# <string.h>, <limits.h> and <stdlib.h> but MinGW-4.x.x does require them.
# (The next point implies 4.x.x is before 4.8.1 because the current port of)
# (MinGW to FreeBSD at 2018-09-29 uses the 4.8.1 toolchain.)
# <errno.h> added in February 2016 after upgrading FreeBSD mingw32 ports,
# and finding it needed on Windows' build using MinGW-5.3.0.
# Do this as well in stdafx.h.
# The make in the MinGW-3.4.5 environment is not able to deal with the
# 'else ifeq' construct, so always doing the '/' normalization helps a lot.
# (Conditional for sed removed because *345* makefile does other option.)

$(V3R0_STDAFX)/%.h : $(SED_STDAFX)/%.h
	sed $(BACK_TO_FORWARD_SLANT) $(SED_STDAFX_H_EDITS) $< > $@

# Copy SWIG interface file from extract directory.

# Include a file which defines dependency and recipe for SWIG interface
# file as close as possible to this file such that the recipe, x86 or
# x64 as appropriate, copies things from extract area to build work area.

# It is hoped this is temporary until problems in the x64 build are
# fixed, when the definition can come back here.


