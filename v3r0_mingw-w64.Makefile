# v3r0_mingw-w64.Makefile
# Run in a shell on a BSD or Linux with Wine installed.

# make -f v3r0_mingw-w64.Makefile
# builds the Python interface to DPT.

# On a BSD usually replace 'make' by 'gmake' in such commands.

DPT_VERSION = v3r0

TOOL_CHAIN = mingw-w64
TOOL_CHAIN_VERSION = 
CPPSTANDARD = c++23
WINE = wine
PATH_TO_CXX =

# Replace win32 by posix and, or, replace x86_64 by i686 for
# alternative environments.
COMPILER = x86_64-w64-mingw32-g++-win32

# Python statement 'import dptdb.dptapi' will report these dlls cannot
# be found if links are not provided in the Python package. 
# Links are created in site-packages/dptdb but boxes other than Debian
# may need different names, and on Debian some, or all, of these names
# will become wrong when later versions of compiler become the default.
OTHER_DLLS_DIRECTORY = /usr/lib/gcc/x86_64-w64-mingw32/14-win32
LIBSTDC = libstdc++-6.dll
LIBGCC_S_SEH = libgcc_s_seh-1.dll

# Used when creating symbolic links to extra DLLs.
USER_SITE_PACKAGES = ~/.wine/drive_c/users/$(USER)/AppData/Roaming/$(PYTHON_NAME)/$(PYTHON_NAME)$(PYTHON_VERSION)/site-packages/dptdb

# Invoked by Wine in BSD or Linux environment.
# Assume default locations.
SWIG_COMMAND = ~/.wine/drive_c/swigwin-4.4.1/swig.exe

# Value of the --platform-tag argument for 'wheel tags ...' command.

# Not sure what PLATFORM_TAG should be for a mingw compiler, perhaps
# mingw_x86_64 like the Msys case, but win_amd64 is likely correct
# for Wine.
PLATFORM_TAG = win_amd64

# Select value from Mk/dpt-dptdb_version for DPT_DPTDB_VERSION.

include Mk/dpt-dptdb_version
DPT_DPTDB_VERSION = $(DPT30_DPTDB_VS_X64)

# sed '-f' arguments.

include Mk/sed_shared_mingw-w64.Mk
include Mk/sed_shared_c++11.Mk
include Mk/sed_shared_64.Mk
include Mk/sed_msys2_64.Mk
include Mk/sed_msys2_clang_64.Mk
include Mk/sed_du1stepinfo_mingw-w64.Mk
include Mk/sed_binary_function.Mk

# Copy, edit, and build.

include Mk/mingw-w64.Mk
include Mk/copy_swig.Mk
