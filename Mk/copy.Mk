# copy.Mk
# Copy source to build version.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION
# PATH_TO_CXX
# COMPILER
# WINE
# where COMPILER is mandatory and will usually be 'cl' or 'mingw32-g++'.

# V3R0, and therefore BUILD and DPT, are defined in v3r0_copy_targets and
# v3r0_mingw_targets.

DPT_LICENCE = licence.txt

# Tests folders.

BUILD_TESTS = $(BUILD)/$(CPP_TESTS)
VR_TESTS = $(BUILD_TESTS)/$(DPT_VERSION)

# Download DPT source from copies of zip files from dptoolkit website
# before it was shut.

# Download site.
DOWNLOAD_URL = http://solentware.co.uk/files/

# Files at download site.
# Downloads, or copies obtained otherwise, are kept as siblings of the
# directory containing this file.
# EXTRACTED is not appropriate for these two names because the distinction
# is versions of DPT DBMS, not reference to extract, copy and build.
# There is a DPT_V3R06_DBMS.ZIP file for example.
SOURCE_ZIP = DPT_V3R0_DBMS.ZIP
DOCUMENTATION_ZIP = DPT_V3R0_DOCS.ZIP

DOCS_EXTRACTED = $(EXTRACT)/docs_v3r0
ATTIC = $(EXTRACTED)/Attic
EXTRACTED_STDAFX = $(EXTRACTED)/stdafx

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
VR_SWIG = $(VR_DIRECTORY)/swig
VR_SWIG_INTERFACE = $(VR_SWIG)/$(SWIG_INTERFACE)
COPY_SWIG = $(EXTRACTED)/$(SWIG_INTERFACE)

DIRECTORY_EXTRACT = @mkdir -p $(EXTRACT)
DIRECTORY_EXTRACTED = @mkdir -p $(EXTRACTED)
DIRECTORY_EXTRACTED_STDAFX = @mkdir -p $(EXTRACTED_STDAFX)

# 'V3R0' source files reference 'stdafx.h' so put the one in 'HelloWorld'
# example in a more fitting location and rename to fit references.
# 'V3R0' is the local name for the stand-alone DBMS available on
# 'dptoolkit.com' until the site ceased to exist.  DBMS is best used as
# the name of the 'V3R06' product, a later version broken in recent
# compliers, copied from
# https://drive.google.com/drive/folders/0B1GLdfqdwpNQUVE0ekFWalEtVHM0

include Mk/extract_from_zip.Mk

clean-extract :
	-rm -rf $(DPT)

$(DOCUMENTATION_ZIP) :
	curl --output $@ $(DOWNLOAD_URL)$(DOCUMENTATION_ZIP)

$(SOURCE_ZIP) :
	curl --output $@ $(DOWNLOAD_URL)$(SOURCE_ZIP)

extract : $(COPY_SWIG)

# Some files, no examples in V3R0, are redundant and must be removed from
# the scope of pattern rules.

# Provide an attic for these files.

# Source file names.

include Mk/source_file_names.Mk

DIRECTORY_VR_TESTS = @mkdir -p $(VR_TESTS)
DIRECTORY_BUILD_TESTS = @mkdir -p $(BUILD_TESTS)
DIRECTORY_BUILD = @mkdir -p $(BUILD)

# Copy service initialization parameters for single step deferred update,
# multi step deferred update, and normal operation.

PARMS_DU_MULTI = parms_dumulti.ini
PARMS_DU_SINGLE = parms_dusingle.ini
PARMS_NORMAL = parms_normal.ini

$(VR_TESTS)/$(PARMS_DU_MULTI) : $(CPP_TESTS)/$(PARMS_DU_MULTI)
	$(DIRECTORY_VR_TESTS)
	cp -p $< $@

$(VR_TESTS)/$(PARMS_DU_SINGLE) : $(CPP_TESTS)/$(PARMS_DU_SINGLE)
	$(DIRECTORY_VR_TESTS)
	cp -p $< $@

$(VR_TESTS)/$(PARMS_NORMAL) : $(CPP_TESTS)/$(PARMS_NORMAL)
	$(DIRECTORY_VR_TESTS)
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

$(VR_SRC)/%.cpp : $(SED_SRC)/%.cpp
	$(DIRECTORY_VR_SRC)
	sed $(SED_SRC_EDITS) $< > $@

$(VR_INC)/%.h : $(SED_INC)/%.h
	$(DIRECTORY_VR_INC)
	sed $(SED_INC_EDITS) $< > $@

$(VR_API_SRC)/%.cpp : $(SED_API_SRC)/%.cpp
	$(DIRECTORY_VR_API_SRC)
	sed $(SED_API_SRC_EDITS) $< > $@

$(VR_API_INC)/%.h : $(SED_API_INC)/%.h
	$(DIRECTORY_VR_API_INC)
	sed $(SED_API_INC_EDITS) $< > $@

$(VR_STDAFX)/%.cpp : $(SED_STDAFX)/%.cpp
	$(DIRECTORY_VR_STDAFX)
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

$(VR_STDAFX)/%.h : $(SED_STDAFX)/%.h
	$(DIRECTORY_VR_STDAFX)
	sed $(BACK_TO_FORWARD_SLANT) $(SED_STDAFX_H_EDITS) $< > $@

# Copy SWIG interface file from extract directory.

# Include a file which defines dependency and recipe for SWIG interface
# file as close as possible to this file such that the recipe, x86 or
# x64 as appropriate, copies things from extract area to build work area.

# It is hoped this is temporary until problems in the x64 build are
# fixed, when the definition can come back here.


