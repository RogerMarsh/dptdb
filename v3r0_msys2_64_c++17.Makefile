# Build V3R0 with c++17 in Msys2 on Microsoft Windows.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = _64
CPPSTANDARD = c++17
WINE =
PATH_TO_CXX =

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_x86_64

# Select value from Mk/dpt30-dptdb_version for DPT30_DPTDB_VERSION.

include Mk/dpt30-dptdb_version
DPT30_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X64)

include Mk/v3r0_sed_shared.Mk
include Mk/v3r0_sed_shared_64.Mk
include Mk/v3r0_sed_msys2_64.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk

