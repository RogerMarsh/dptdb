# vs_copy_64.Mk
# Copy source for build with c++ in a Microsoft VS 64 bit environment.

# Compiler settings.

PATH_TO_CXX =
WINE =

# Copy and edit.

include Mk/vs_targets.Mk
include Mk/copy.Mk
include Mk/copy_swig_64.Mk

