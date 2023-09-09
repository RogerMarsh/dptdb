# Build V3R0 with c++98 in Msys2 on Microsoft Windows.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++98
WINE =
PATH_TO_CXX =

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_i686

include Mk/v3r0_sed_shared.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk

