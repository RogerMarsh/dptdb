# Build V3R0 with c++14 in Msys2 on Microsoft Windows.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = _64
CPPSTANDARD = c++14
WINE =
PATH_TO_CXX =

include Mk/v3r0_sed_shared.Mk
include Mk/v3r0_sed_shared_64.Mk
include Mk/v3r0_sed_msys2_64.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk

