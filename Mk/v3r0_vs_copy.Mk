# Copy V3R0 for build with c++ in a Microsoft Visual Studio environment.

# Compiler settings.

PATH_TO_CXX =
WINE =

# sed '-f' arguments.

include Mk/v3r0_sed_shared.Mk

# Copy and edit.

include Mk/v3r0_copy_targets.Mk
include Mk/v3r0_copy.Mk
include Mk/v3r0_copy_swig.Mk
include Mk/v3r0_source_targets.Mk

