# Copy V3R0 binary_function edits for standards earlier than c++11.

$(V3R0)/binary_function : $(V3R0_INC)/stlextra.h $(V3R0_SRC)/findwork.cpp
	touch $@
