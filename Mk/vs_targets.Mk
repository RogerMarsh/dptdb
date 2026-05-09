# vs_targets.Mk
# Source copy targets.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION

# DPT extract and build folders.
# Most are defined in copy.Mk but some are needed here.

include Mk/dpt.Mk

BUILD = $(DPT)/$(TOOL_CHAIN)$(TOOL_CHAIN_VERSION)_$(COMPILER)_$(CPPSTANDARD)
VR_DIRECTORY = $(BUILD)/$(DPT_VERSION)

# Main targets (phony copy targets are defined near the real targets).

.PHONY : all clean copy-all clean-objects clean-extract extract

all : copy-all

clean :
	-rm -r $(VR_DIRECTORY)

clean-objects :
	-rm -r $(VR_DIRECTORY)/object

