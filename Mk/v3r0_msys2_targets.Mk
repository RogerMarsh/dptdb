# V3R0 targets.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION

# DPT extract and build folders.
# Most are defined in v3r0_copy.Mk but some are needed here.

include Mk/v3r0_dpt.Mk

DPT_VERSION = v3r0
BUILD = $(DPT)/$(TOOL_CHAIN)$(TOOL_CHAIN_VERSION)_$(CPPSTANDARD)
V3R0 = $(BUILD)/$(DPT_VERSION)
V3R0_OBJECT = $(V3R0)/object
V3R0API_OBJECT = $(V3R0_OBJECT)/dbapi
V3R0STDAFX_OBJECT = $(V3R0_OBJECT)/stdafx
V3R0SWIG_OBJECT = $(V3R0_OBJECT)/swig
V3R0_PACKAGE = $(V3R0)/package
V3R0_PACKAGE_DPTDB = $(V3R0_PACKAGE)/src/dptdb

# Main targets (phony build targets are defined near the build targets).

.PHONY : all clean wrapper local-install tests clean-tests rebuild-tests

all : wrapper

clean :
	-rm -r $(V3R0)

