# Copy V3R0 binary_function edits for standard c++11 and later.

$(V3R0)/stlextra_h_bf : $(V3R0_INC)/stlextra.h
	sed -i -f sedCommands/NoCaseSortPredicate $<
	touch $@

$(V3R0)/findwork_cpp_bf : $(V3R0_SRC)/findwork.cpp
	sed -i -f sedCommands/LeafInfoLessThanPredicate $<
	touch $@

$(V3R0)/binary_function : $(V3R0)/stlextra_h_bf $(V3R0)/findwork_cpp_bf
	touch $@
