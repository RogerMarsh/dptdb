# Copy V3R0 for build with c++20 in Microsoft VS 2022 x64 environment.

# The makefile naming convention arose from using Developer Command Prompt
# to do the initial work getting 32 bit DPT running again.

# A consequence is the naming convention for these makefiles appends '_32'
# to the Python element of the name for x86 (32 bit) builds, but '_64' to
# the Visual Studio element of the name for x64 (64 bit) builds.


TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 2022_64
CPPSTANDARD = c++20
COMPILER = cl

# sed '-f' arguments.

include Mk/v3r0_vs_sed_64.Mk

# Copy and edit.

include Mk/v3r0_vs_copy_64.Mk
include Mk/v3r0_copy_binary_function.Mk
include Mk/v3r0_copy_all.Mk

