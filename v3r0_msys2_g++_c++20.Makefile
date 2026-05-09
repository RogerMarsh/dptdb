# v3r0_msys2_g++_c++20.Makefile
# Run in a Msys2 MINGW32 shell on Microsoft Windows.
# (The MINGW32 environment is deprecated at 2023-12-13.)

# make -f v3r0_msys2_g++_c++20.Makefile
# builds the Python interface to DPT.

# make -f v3r0_msys2_g++_c++20.Makefile tests
# builds the C++ tests of DPT.

DPT_VERSION = v3r0

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++20
WINE =
PATH_TO_CXX =
COMPILER = g++

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_i686_msvcrt_gnu

# Select value from Mk/dpt-dptdb_version for DPT_DPTDB_VERSION.

include Mk/dpt-dptdb_version
DPT_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X86)

# sed '-f' arguments.

include Mk/sed_shared.Mk
include Mk/sed_shared_c++11.Mk
include Mk/sed_binary_function.Mk

# Copy, edit, and build.

include Mk/msys2.Mk
include Mk/copy_swig.Mk
