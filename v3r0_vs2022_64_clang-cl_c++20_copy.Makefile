# v3r0_vs2022_64_clang-cl_c++20_copy.Makefile
# Run in a Msys2 MSYS shell on Microsoft Windows.

# make -f v3r0_vs2022_64_clang-cl_c++20_copy.Makefile
# copies the source code to the appropriate clang-cl build directory.

# Assumes fetch.Makefile has been run.

# The makefile naming convention arose from using Developer Command Prompt
# to do the initial work getting 32 bit DPT running again.

# A consequence is the naming convention for these makefiles appends '_32'
# to the Python element of the name for x86 (32 bit) builds, but '_64' to
# the Visual Studio element of the name for x64 (64 bit) builds.


TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 2022_64
CPPSTANDARD = c++20
COMPILER = clang-cl

# sed '-f' arguments.

include Mk/v3r0_vs_sed_64.Mk
include Mk/v3r0_sed_du1stepinfo.Mk
include Mk/v3r0_sed_binary_function.Mk
include Mk/v3r0_sed_resource_lockinfo.Mk
include Mk/v3r0_vs_sed_ord_comp_ptr_int.Mk

# Copy and edit.

include Mk/v3r0_vs_copy_64.Mk
include Mk/v3r0_copy_all.Mk

