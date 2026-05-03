# v3r0_msys2_64_g++_c++98.Makefile
# Run in a Msys2 UCRT64 shell on Microsoft Windows.

# make -f v3r0_msys2_64_g++_c++98.Makefile
# builds the Python interface to DPT.

# make -f v3r0_msys2_64_g++_c++98.Makefile tests
# builds the C++ tests of DPT.

# Assumes fetch.Makefile has been run.

TOOL_CHAIN = msys2
TOOL_CHAIN_VERSION = _64
CPPSTANDARD = c++98
WINE =
PATH_TO_CXX =
COMPILER = g++

# Value of the --platform-tag argument for 'wheel tags ...' command.

PLATFORM_TAG = mingw_x86_64_msvcrt_gnu

# Select value from Mk/dpt30-dptdb_version for DPT30_DPTDB_VERSION.

include Mk/dpt30-dptdb_version
DPT30_DPTDB_VERSION = $(DPT30_DPTDB_MSYS2_X64)

# sed '-f' arguments.
# The *_c++11.Mk file is included because the feature provided by
# it's #include directive is needed.  Including this file gives a
# more useful error message than the multitude of error messages
# when it is absent.

include Mk/v3r0_sed_shared.Mk
include Mk/v3r0_sed_shared_c++11.Mk
include Mk/v3r0_sed_shared_64.Mk
include Mk/v3r0_sed_msys2_64.Mk

# Copy, edit, and build.

include Mk/v3r0_msys2.Mk
include Mk/v3r0_copy_swig.Mk
