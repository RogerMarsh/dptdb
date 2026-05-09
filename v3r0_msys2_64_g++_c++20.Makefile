# v3r0_msys2_64_g++_c++20.Makefile
# Run in a Msys2 UCRT64 shell on Microsoft Windows.

# make -f v3r0_msys2_64_g++_c++20.Makefile
# builds the Python interface to DPT.

# make -f v3r0_msys2_64_g++_c++20.Makefile tests
# builds the C++ tests of DPT.

DPT_VERSION = v3r0

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = _64
CPPSTANDARD = c++20
WINE =
PATH_TO_CXX =
COMPILER = g++

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_x86_64_msvcrt_gnu

# Select value from Mk/dpt-dptdb_version for DPT_DPTDB_VERSION.

include Mk/dpt-dptdb_version
DPT_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X64)

# sed '-f' arguments.

include Mk/sed_shared.Mk
include Mk/sed_shared_c++11.Mk
include Mk/sed_shared_64.Mk
include Mk/sed_msys2_64.Mk
include Mk/sed_du1stepinfo.Mk
include Mk/sed_binary_function.Mk

# Copy, edit, and build.

include Mk/msys2.Mk
include Mk/copy_swig.Mk
