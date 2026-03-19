# The copy-all target for build with c++ in a Microsoft Visual Studio environment.

# Cannot delay copying SWIG stuff because the build is done by nmake.
# The make for msys2 does not need the 'copy-all' indirection.
# V3R0_SWIG and SWIG_INTERFACE are defined in Mk/v3r0_copy.Mk.

# The 'binary function' edits cannot be done by a sequence of single
# line sed 'replace in context' commands.
# Cannot delay binary_function edits because all must be done before
# any source is compiled.
# Therefore the make for msys2 needs the copy-all target despite
# being unnecessary for SWIG purposes.

copy-all : $(SOURCE_FILES) $(V3R0)/binary_function $(V3R0_SWIG)/$(SWIG_INTERFACE) $(V3R0_TESTS) $(V3R0_TESTS)/$(PARMS_DU_SINGLE)
