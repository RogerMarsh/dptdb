# v3r06_vs_copy.Makefile
# Run in a Msys2 MSYS shell on Microsoft Windows.

# make -f v3r06_vs_copy.Makefile
# copies the source code to build directory.

# Assumes extract-v3r06.Makefile has been run.

TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 
CPPSTANDARD = 
COMPILER = 

# sed '-f' arguments.

# Copied from Mk/v3r0_sed_shared.Mk via Mk/v3r0_vs_sed_64.Mk and adjusted.

SED_STDAFX_H_EDITS = -f sedCommands/extra_h_stdafx_c++14
SED_SRC_EDITS = -f sedCommands/back_to_forward_slant \
                -f sedCommands/make_pair \
                -f sedCommands/access_controller \
                -f sedCommands/i64_to_ll \
                -f sedCommands/comment_session \
                -f sedCommands/ord_comp_ptr_int \
                -f sedCommands/fastload_no_upper \
                -f sedCommands/msgini_restore_upper \
                -f sedCommands/resource_cpp_lockinfo
SED_INC_EDITS = -f sedCommands/back_to_forward_slant \
                -f sedCommands/resource_h_lockinfo
SEDAPI_SRC_EDITS = -f sedCommands/back_to_forward_slant
SEDAPI_INC_EDITS = -f sedCommands/back_to_forward_slant
SED_STDAFX_CPP_EDITS = -f sedCommands/back_to_forward_slant

# Copied from Mk/v3r0_sed_shared_64.Mk via Mk/v3r0_vs_sed_64.Mk and adjusted.

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

# Copied from Mk/v3r0_sed_binary_function.Mk and adjusted.

SED_SRC_EDITS += \
                -f sedCommands/LeafInfoLessThanPredicate

SED_INC_EDITS += \
                -f sedCommands/NoCaseSortPredicate \
                -f sedCommands/FieldValueLessThanPredicate

# Copy and edit.

# Copied from Mk/v3r0_vs_copy_64.Mk and adjusted.

PATH_TO_CXX =
WINE =

# Copied from Mk/v3r0_copy_targets.Mk and adjusted.

# DPT extract and build folders.
# Most are defined in v3r0_copy.Mk but some are needed here.

include Mk/v3r06_dpt.Mk

BUILD = $(DPT)/$(TOOL_CHAIN)
V3R06 = $(BUILD)/$(DPT_VERSION)

# Main targets (phony copy targets are defined near the real targets).

.PHONY : all clean copy-all clean-objects

all : copy-all

clean :
	-rm -r $(V3R06)

clean-objects :
	-rm -r $(V3R06)/object

# Copied from include Mk/v3r0_copy.Mk and adjusted.

DPT_LICENCE = licence.txt

# DPT extract and build folders.

V3R06_SRC = $(V3R06)/source
V3R06_INC = $(V3R06)/include
V3R06API_SRC = $(V3R06_SRC)/dbapi
V3R06API_INC = $(V3R06_INC)/dbapi
V3R06_STDAFX = $(V3R06)/stdafx
SED_SRC = $(V3R06E)/source
SED_INC = $(V3R06E)/include
SEDAPI_SRC = $(SED_SRC)/dbapi
SEDAPI_INC = $(SED_INC)/dbapi
SED_STDAFX = $(V3R06E)/stdafx

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
V3R06_SWIG = $(V3R06)/swig
V3R06_SWIG_INTERFACE = $(V3R06_SWIG)/$(SWIG_INTERFACE)
COPY_SWIG = $(V3R06E)/$(SWIG_INTERFACE)

# Source file names.

SED_NAMES = $(basename $(notdir $(wildcard $(SED_SRC)/*.cpp)))

SEDAPI_NAMES = $(basename $(notdir $(wildcard $(SEDAPI_SRC)/*.cpp)))

SED_INC_NAMES = $(basename $(notdir $(wildcard $(SED_INC)/*.h)))

SEDAPI_INC_NAMES = $(basename $(notdir $(wildcard $(SEDAPI_INC)/*.h)))

SEDAFX_NAMES = stdafx

SRCS = $(SED_NAMES:%=$(V3R06_SRC)/%.cpp)

API_SRCS = $(SEDAPI_NAMES:%=$(V3R06API_SRC)/%.cpp)

INCS = $(SED_INC_NAMES:%=$(V3R06_INC)/%.h)

API_INCS = $(SEDAPI_INC_NAMES:%=$(V3R06API_INC)/%.h)

AFX_SRCS = $(SEDAFX_NAMES:%=$(V3R06_STDAFX)/%.cpp)

AFX_INCS = $(SEDAFX_NAMES:%=$(V3R06_STDAFX)/%.h)

SOURCE_FILES = $(SRCS) $(INCS) $(API_SRCS) $(API_INCS) $(AFX_SRCS) $(AFX_INCS)

# The build directory parent (dpt/v3r0) is created in extract-v3r06.Makefile.

$(V3R06API_SRC) : $(V3R06_SRC)
	-mkdir $(V3R06API_SRC)

$(V3R06_SRC) : $(V3R06)
	-mkdir $(V3R06_SRC)

$(V3R06API_INC) : $(V3R06_INC)
	-mkdir $(V3R06API_INC)

$(V3R06_INC) : $(V3R06)
	-mkdir $(V3R06_INC)

$(V3R06_STDAFX) : $(V3R06)
	-mkdir $(V3R06_STDAFX)

$(V3R06_SWIG) : $(V3R06)
	-mkdir $(V3R06_SWIG)

$(V3R06) : $(BUILD)
	-mkdir $(V3R06)

$(BUILD) :
	-mkdir $(BUILD)

# Pattern rules for editing DPT C++.

$(V3R06_SRC)/%.cpp : $(SED_SRC)/%.cpp
	sed $(SED_SRC_EDITS) $< > $@

$(V3R06_INC)/%.h : $(SED_INC)/%.h
	sed $(SED_INC_EDITS) $< > $@

$(V3R06API_SRC)/%.cpp : $(SEDAPI_SRC)/%.cpp
	sed $(SEDAPI_SRC_EDITS) $< > $@

$(V3R06API_INC)/%.h : $(SEDAPI_INC)/%.h
	sed $(SEDAPI_INC_EDITS) $< > $@

$(V3R06_STDAFX)/%.cpp : $(SED_STDAFX)/%.cpp
	sed $(SED_STDAFX_CPP_EDITS) $< > $@

$(V3R06_STDAFX)/%.h : $(SED_STDAFX)/%.h
	sed $(BACK_TO_FORWARD_SLANT) $(SED_STDAFX_H_EDITS) $< > $@

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
V3R06_SWIG = $(V3R06)/swig
V3R06_SWIG_INTERFACE = $(V3R06_SWIG)/$(SWIG_INTERFACE)
COPY_SWIG = $(V3R06E)/$(SWIG_INTERFACE)

# Source file names.

# The build directory parent (dpt/v3r0) is created in fetch.Makefile.

$(V3R06_SWIG) : $(V3R06)
	-mkdir $(V3R06_SWIG)

# Copied from Mk/v3r0_copy_swig.Mk and adjusted.

$(V3R06_SWIG)/$(SWIG_INTERFACE) : $(COPY_SWIG)
	-mkdir $(V3R06_SWIG)
	cp -p $< $@

# Copied from Mk/v3r0_source_targets.Mk and adjusted.

$(SRCS) : $(V3R06_SRC)

$(INCS) : $(V3R06_INC)

$(API_SRCS) : $(V3R06API_SRC)

$(API_INCS) : $(V3R06API_INC)

$(AFX_SRCS) : $(V3R06_STDAFX)

$(AFX_INCS) : $(V3R06_STDAFX)

# Copied from Mk/v3r0_copy_all.Mk and adjusted.

copy-all : $(SOURCE_FILES) $(V3R06_SWIG)/$(SWIG_INTERFACE)

