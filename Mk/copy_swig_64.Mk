# copy_swig_64.Mk
# Copy SWIG interface file from extract directory for x64.

# Include this file immediately after Mk/copy.Mk in makefiles
# which are involved in building x64 version in Visual Studio
# environment.

# Include this file immediately after Mk/msys2.Mk in makefiles
# which are involved in building x64 version in Msys2 environment.

$(VR_SWIG_INTERFACE) : $(COPY_SWIG)
	-mkdir $(VR_SWIG)
	sed -f sedCommands/swig_no_dusingle_x64 $< > $@


