# Source file targets.

# These targets must be available for 'copy only' and 'copy and build'.

# Build targets (.PHONY).

directories : $(V3R0API_SRC) $(V3R0API_INC) $(V3R0_STDAFX) $(V3R0_SWIG)

source_files : $(SRCS) $(INCS) $(API_SRCS) $(API_INCS) $(AFX_SRCS) $(AFX_INCS) $(V3R0_SWIG_I)

