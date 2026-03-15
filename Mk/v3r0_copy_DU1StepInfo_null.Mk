# Move implementation of IsInitialized() from du1step.h to du1step.cpp
# to avoid 'error: arithmetic on a pointer to an incomplete type ...'
# first seen in 64-bit clang c++20 compilations.

$(V3R0)/du1step_stepinfo : $(V3R0_INC)/du1step.h $(V3R0_SRC)/du1step.cpp
	touch $@
