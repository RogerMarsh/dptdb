# v3r0_msys2_g++_c++14.Makefile
# Run in a Msys2 MINGW32 shell on Microsoft Windows.
# (The MINGW32 environment is deprecated at 2023-12-13.)

# make -f v3r0_msys2_g++_c++14.Makefile
# builds the Python interface to DPT.

# make -f v3r0_msys2_g++_c++14.Makefile tests
# builds the C++ tests of DPT.

# Assumes fetch.Makefile has been run.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++14
WINE =
PATH_TO_CXX =
COMPILER = g++

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_i686_msvcrt_gnu

# Select value from Mk/dpt30-dptdb_version for DPT30_DPTDB_VERSION.

include Mk/dpt30-dptdb_version
DPT30_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X86)

# sed '-f' arguments.

include Mk/v3r0_sed_shared.Mk
include Mk/v3r0_sed_shared_c++11.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk
include Mk/v3r0_copy_swig.Mk
