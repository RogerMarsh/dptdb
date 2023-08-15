# Build V3R0 with c++14 in Msys2 on Microsoft Windows.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++14
WINE =
PATH_TO_CXX =

include Mk/v3r0_sed_shared.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk

