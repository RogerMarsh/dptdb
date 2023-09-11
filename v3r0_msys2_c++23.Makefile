# Build V3R0 with c++23 in Msys2 on Microsoft Windows.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++23
WINE =
PATH_TO_CXX =

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_i686

# Select value from Mk/dpt30-dptdb_version for DPT30_DPTDB_VERSION.

include Mk/dpt30-dptdb_version
DPT30_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X86)

include Mk/v3r0_sed_shared.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk

