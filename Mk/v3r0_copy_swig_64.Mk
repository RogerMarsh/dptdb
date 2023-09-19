# Copy SWIG interface file from extract directory for x64.

# Include this file immediately after Mk/v3r0_copy.Mk in makefiles
# which are involved in building x64 version in Visual Studio
# environment.

# Include this file immediately after Mk/v3r0_msys2.Mk in makefiles
# which are involved in building x64 version in Msys2 environment.

$(V3R0_SWIG)/$(SWIG_INTERFACE) : $(COPY_SWIG)
	-mkdir $(V3R0_SWIG)
	sed -f sedCommands/swig_no_dusingle_x64 $< > $@


