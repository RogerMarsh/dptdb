# v3r0_vs_sed_ord_comp_ptr_int.Mk
# Additional 'sed' '-f' arguments for pointer comparison in winutil.cpp.
# This edit is required by all Msys2 g++ and clang++ builds, but only
# in VS 2026 build at c++latest standard (of the ones tried).
# The Msys2 edit is requested in v3r0_sed_shared.Mk as the only *.cpp
# edit.

SED_SRC_EDITS += -f sedCommands/ord_comp_ptr_int
