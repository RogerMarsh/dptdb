# Copy V3R0 for build with c++20 in Microsoft VS 2022 x86 environment.

# The makefile naming convention arose from using Developer Command Prompt
# to do the initial work getting 32 bit DPT running again.

# A consequence is appending '_32' to the Python element of the name, if
# there is one, for x86 (32 bit) builds; but '_64' to the Visual Studio
# element of the name for x64 (64 bit) builds.

TOOL_CHAIN = vs
TOOL_CHAIN_VERSION = 2022
CPPSTANDARD = c++20

# Copy and edit.

include Mk/v3r0_vs_copy.Mk

