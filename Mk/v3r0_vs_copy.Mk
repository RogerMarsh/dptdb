# Copy V3R0 for build with c++ in a Microsoft Visual Studio environment.

# Compiler settings.

PATH_TO_CXX =
COMPILER = cl
WINE =

# sed '-f' arguments.

include Mk/v3r0_sed_shared.Mk

# Copy and edit.

include Mk/v3r0_copy_targets.Mk
include Mk/v3r0_copy.Mk
include Mk/v3r0_source_targets.Mk

# Cannot delay copying SWIG stuff because the build is done by nmake.
# The make for msys2 does not need the 'copy-all' indirection.
# V3R0_SWIG and SWIG_INTERFACE are defined in Mk/v3r0_copy.Mk.

copy-all : directories source_files $(V3R0_SWIG)/$(SWIG_INTERFACE)
