# v3r06_vs_copy.Makefile
# Run in a Msys2 MSYS shell on Microsoft Windows.

# make -f v3r06_vs_copy.Makefile
# copies the source code to build directory.

DPT_VERSION = v3r06

TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 
CPPSTANDARD = 
COMPILER = 

# sed '-f' arguments.

# The extra_h_stdafx_64_c++98 edit causes all c++98 and c++03 builds
# to fail on Msys2 builds; but these standards are not now readily
# available for VS builds.

SED_STDAFX_H_EDITS = -f sedCommands/extra_h_stdafx_c++98 \
                     -f sedCommands/extra_h_stdafx_c++11 \
                     -f sedCommands/extra_h_stdafx_64_c++98
SED_SRC_EDITS = -f sedCommands/make_pair \
                -f sedCommands/access_controller \
                -f sedCommands/i64_to_ll \
                -f sedCommands/comment_session \
                -f sedCommands/ord_comp_ptr_int \
                -f sedCommands/fastload_no_upper \
                -f sedCommands/msgini_restore_upper \
                -f sedCommands/resource_cpp_lockinfo
SED_INC_EDITS = -f sedCommands/resource_h_lockinfo
SED_API_SRC_EDITS = -f /dev/null
SED_API_INC_EDITS = -f /dev/null
SED_STDAFX_CPP_EDITS = -f /dev/null

SED_SRC_EDITS += -f sedCommands/bitmap3_cpp_01\
                 -f sedCommands/bitmap3_cpp_02\
                 -f sedCommands/bitmap3_cpp_03\
                 -f sedCommands/bitmap3_cpp_04\
                 -f sedCommands/bitmap3_cpp_05\
                 -f sedCommands/bitmap3_cpp_06\
                 -f sedCommands/bitmap3_cpp_07\
                 -f sedCommands/bitmap3_cpp_08\
                 -f sedCommands/bitmap3_cpp_09\
                 -f sedCommands/bitmap3_cpp_10\
                 -f sedCommands/bitmap3_cpp_11\
                 -f sedCommands/bitmap3_cpp_12\
                 -f sedCommands/bitmap3_cpp_13\
                 -f sedCommands/bitmap3_cpp_14\
                 -f sedCommands/bitmap3_cpp_15\
                 -f sedCommands/bitmap3_cpp_16\
                 -f sedCommands/bitmap3_cpp_17\
                 -f sedCommands/bitmap3_cpp_18\
                 -f sedCommands/bitmap3_cpp_19\
                 -f sedCommands/bitmap3_cpp_20\
                 -f sedCommands/bitmap3_cpp_21\
                 -f sedCommands/bitmap3_cpp_22\
                 -f sedCommands/bitmap3_cpp_23\
                 -f sedCommands/bitmap3_cpp_24\
                 -f sedCommands/bitmap3_cpp_25\
                 -f sedCommands/bitmap3_cpp_26\
                 -f sedCommands/bitmap3_cpp_27\
                 -f sedCommands/bitmap3_cpp_28\
                 -f sedCommands/bitmap3_cpp_29\
                 -f sedCommands/bitmap3_cpp_30\
                 -f sedCommands/bitmap3_cpp_31\
                 -f sedCommands/bitmap3_cpp_32\
                 -f sedCommands/bitmap3_cpp_33\
                 -f sedCommands/bitmap3_cpp_34\
                 -f sedCommands/bitmap3_cpp_35\
                 -f sedCommands/bitmap3_cpp_36\
                 -f sedCommands/bitmap3_cpp_37\
                 -f sedCommands/bitmap3_cpp_38\
                 -f sedCommands/bitmap3_cpp_39\
                 -f sedCommands/bitmap3_cpp_40\
                 -f sedCommands/bitmap3_cpp_41\
                 -f sedCommands/bitmap3_cpp_42\
                 -f sedCommands/bitmap3_cpp_43\
                 -f sedCommands/bitmap3_cpp_44\
                 -f sedCommands/bitmap3_cpp_45\
                 -f sedCommands/bitmap3_cpp_46

SED_INC_EDITS += -f sedCommands/bitmap3_h_01\
                 -f sedCommands/bitmap3_h_02\
                 -f sedCommands/bitmap3_h_03\
                 -f sedCommands/bitmap3_h_04\
                 -f sedCommands/bitmap3_h_05\
                 -f sedCommands/bitmap3_h_06\
                 -f sedCommands/bitmap3_h_07\
                 -f sedCommands/bitmap3_h_08\
                 -f sedCommands/bitmap3_h_09\
                 -f sedCommands/bitmap3_h_10\
                 -f sedCommands/bitmap3_h_11\
                 -f sedCommands/bitmap3_h_12\
                 -f sedCommands/bitmap3_h_13\
                 -f sedCommands/bitmap3_h_14\
                 -f sedCommands/bitmap3_h_15\
                 -f sedCommands/bitmap3_h_16\
                 -f sedCommands/bitmap3_h_17\
                 -f sedCommands/bitmap3_h_18\
                 -f sedCommands/bitmap3_h_19\
                 -f sedCommands/bitmap3_h_20\
                 -f sedCommands/bitmap3_h_21\
                 -f sedCommands/bitmap3_h_22\
                 -f sedCommands/bitmap3_h_23\
                 -f sedCommands/bitmap3_h_24\
                 -f sedCommands/du1seginvlist_01\
                 -f sedCommands/du1seginvlist_02\
                 -f sedCommands/du1seginvlist_03

SED_SRC_EDITS += \
                -f sedCommands/LeafInfoLessThanPredicate

SED_INC_EDITS += \
                -f sedCommands/NoCaseSortPredicate \
                -f sedCommands/FieldValueLessThanPredicate

# Copy and edit.

PATH_TO_CXX =
WINE =

# File containing the v3r06 source code.
SOURCE_ZIP = DPT_V3R06_DBMS.ZIP

# File containing the v3r0 documentation.
DOCUMENTATION_ZIP = DPT_V3R0_DOCS.ZIP

# DPT extract and build folders.

include Mk/dpt.Mk

# For specific files which have to be renamed or moved to attic.
ATTIC = $(EXTRACTED)/Attic

DOCS_EXTRACTED = $(EXTRACT)/docs_v3r0
EXTRACTED_STDAFX = $(EXTRACTED)/stdafx

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
COPY_SWIG = $(EXTRACTED)/$(SWIG_INTERFACE)

DIRECTORY_EXTRACT = @mkdir -p $(EXTRACT)
DIRECTORY_EXTRACTED = @mkdir -p $(EXTRACTED)
DIRECTORY_EXTRACTED_STDAFX = @mkdir -p $(EXTRACTED_STDAFX)

BUILD = $(DPT)/$(TOOL_CHAIN)
VR_DIRECTORY = $(BUILD)/$(DPT_VERSION)

# Main targets (phony copy targets are defined near the real targets).

.PHONY : all clean copy-all clean-objects clean-extract extract

all : copy-all

clean :
	-rm -r $(VR_DIRECTORY)

clean-objects :
	-rm -r $(VR_DIRECTORY)/object

extract : $(COPY_SWIG)

DPT_LICENCE = licence.txt

clean-extract :
	-rm -rf $(DPT)

include Mk/extract_from_zip.Mk

# The *.i file defining the SWIG interface.
VR_SWIG = $(VR_DIRECTORY)/swig
VR_SWIG_INTERFACE = $(VR_SWIG)/$(SWIG_INTERFACE)

# Source file names.

include Mk/source_file_names.Mk

# Pattern rules for editing DPT C++.

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

$(VR_STDAFX)/%.h : $(SED_STDAFX)/%.h
	$(DIRECTORY_VR_STDAFX)
	sed $(BACK_TO_FORWARD_SLANT) $(SED_STDAFX_H_EDITS) $< > $@

# The *.i file defining the SWIG interface.
VR_SWIG = $(VR_DIRECTORY)/swig

$(VR_SWIG_INTERFACE) : $(COPY_SWIG)
	$(DIRECTORY_VR_SWIG)
	cp -p $< $@

copy-all : $(VR_SWIG_INTERFACE) $(SOURCE_FILES)
ifeq ($(strip $(wildcard $(EXTRACTED))),)
	$(error Extract from zip file completed: rerun this job to continue)
endif
	$(error Copy to build directory completed: run matching nmake in correct Visual Studio shell to continue)

