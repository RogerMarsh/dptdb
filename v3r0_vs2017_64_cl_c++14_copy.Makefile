# v3r0_vs2017_64_cl_c++14_copy.Makefile
# Run in a Msys2 MSYS shell on Microsoft Windows.

# make -f v3r0_vs2017_64_cl_c++14_copy.Makefile
# copies the source code to the appropriate cl build directory.

# Assumes fetch.Makefile has been run.

# The makefile naming convention arose from using Developer Command Prompt
# to do the initial work getting 32 bit DPT running again.

# A consequence is the naming convention for these makefiles appends '_32'
# to the Python element of the name for x86 (32 bit) builds, but '_64' to
# the Visual Studio element of the name for x64 (64 bit) builds.

DPT_VERSION = v3r0

TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 2017_64
CPPSTANDARD = c++14
COMPILER = cl

# sed '-f' arguments.

include Mk/vs_sed_64.Mk

# Copy and edit.

include Mk/vs_copy.Mk
include Mk/copy_all.Mk

