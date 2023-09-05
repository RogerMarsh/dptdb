# Source file targets.

# These targets must be available for 'copy only' and 'copy and build'.

$(SRCS) : $(V3R0_SRC)

$(INCS) : $(V3R0_INC)

$(API_SRCS) : $(V3R0API_SRC)

$(API_INCS) : $(V3R0API_INC)

$(AFX_SRCS) : $(V3R0_STDAFX)

$(AFX_INCS) : $(V3R0_STDAFX)

