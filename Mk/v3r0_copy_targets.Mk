# V3R0 copy targets.

# Include this file in a makefile that defines these variables:
# TOOL_CHAIN_VERSION

# DPT extract and build folders.
# Most are defined in v3r0_copy.Mk but some are needed here.

include Mk/v3r0_dpt.Mk

BUILD = $(DPT)/$(TOOL_CHAIN)$(TOOL_CHAIN_VERSION)_$(CPPSTANDARD)
V3R0 = $(BUILD)/$(DPT_VERSION)

# Main targets (phony copy targets are defined near the real targets).

.PHONY : all clean copy-all clean-objects

all : copy-all

clean :
	-rm -r $(V3R0)

clean-objects :
	-rm -r $(V3R0)/object

