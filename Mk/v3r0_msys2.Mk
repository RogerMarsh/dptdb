# Build V3R0 with Msys2 on Microsoft Windows.

# Compiler settings.

COMPILER = g++

# Copy, edit, and build.

include Mk/v3r0_msys2_targets.Mk
include Mk/v3r0_copy.Mk
include Mk/v3r0_msys2_build.Mk
include Mk/v3r0_source_targets.Mk

