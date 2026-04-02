# v3r0_vs2026_64_cl_c++latest_copy.Makefile
# Run in a Msys2 MSYS shell on Microsoft Windows.

# make -f v3r0_vs2026_64_cl_c++latest_copy.Makefile
# copies the source code to the appropriate cl build directory.

# Assumes fetch.Makefile has been run.

# The makefile naming convention arose from using Developer Command Prompt
# to do the initial work getting 32 bit DPT running again.

# A consequence is the naming convention for these makefiles appends '_32'
# to the Python element of the name for x86 (32 bit) builds, but '_64' to
# the Visual Studio element of the name for x64 (64 bit) builds.


TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 2026_64
CPPSTANDARD = c++latest
COMPILER = cl

# sed '-f' arguments.

include Mk/v3r0_vs_sed_64.Mk
include Mk/v3r0_sed_binary_function.Mk

# Copy and edit.

include Mk/v3r0_vs_copy_64.Mk
include Mk/v3r0_copy_all.Mk

