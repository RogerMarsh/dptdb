# copy_all.Mk
# The copy-all target for builds in Visual Studio or Mingw-w64.
# Mingw-w64 covers builds under Wine (unix) and Msys2 (MS Windows).

# Cannot delay copying SWIG stuff because the build is done by nmake.
# The make for msys2 does not need the 'copy-all' indirection.
# VR_SWIG and SWIG_INTERFACE are defined in Mk/copy.Mk.

# The SOURCE_FILES element is after the SWIG_INTERFACE element
# because the extract from zip file stage is done as part of the
# SWIG_INTERFACE rule.

copy-all : $(VR_SWIG_INTERFACE) $(SOURCE_FILES) $(VR_TESTS)/$(PARMS_DU_SINGLE) $(VR_TESTS)/$(PARMS_NORMAL) $(VR_TESTS)/$(PARMS_DU_MULTI)
ifeq ($(strip $(wildcard $(EXTRACTED))),)
	$(error Extract from zip file completed: rerun this job to continue)
endif
ifeq ($(COMPILER), cl)
	$(error Copy to build directory completed: run matching nmake in correct Visual Studio shell to continue)
endif
ifeq ($(COMPILER), clang-cl)
	$(error Copy to build directory completed: run matching nmake in correct Visual Studio shell to continue)
endif
