# vs_copy.Mk
# Copy source for build with c++ in a Microsoft Visual Studio environment.

# Compiler settings.

PATH_TO_CXX =
WINE =

# Copy and edit.

include Mk/vs_targets.Mk
include Mk/copy.Mk
include Mk/copy_swig.Mk

