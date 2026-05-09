# msys2_targets.Mk
# Version targets.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION

# DPT extract and build folders.
# Most are defined in copy.Mk but some are needed here.

include Mk/dpt.Mk

BUILD = $(DPT)/$(TOOL_CHAIN)$(TOOL_CHAIN_VERSION)_$(COMPILER)_$(CPPSTANDARD)
VR_DIRECTORY = $(BUILD)/$(DPT_VERSION)
VR_OBJECT = $(VR_DIRECTORY)/object
VR_API_OBJECT = $(VR_OBJECT)/dbapi
VR_STDAFX_OBJECT = $(VR_OBJECT)/stdafx
VR_SWIG_OBJECT = $(VR_OBJECT)/swig
VR_PACKAGE = $(VR_DIRECTORY)/package
VR_PACKAGE_DPTDB = $(VR_PACKAGE)/src/dptdb

# Main targets (phony build targets are defined near the build targets).

.PHONY : all clean wrapper local-install tests copy-all

all : copy-all wrapper

clean :
	-rm -r $(VR_DIRECTORY)

