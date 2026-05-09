# copy_swig.Mk
# Copy SWIG interface file from extract directory for x86.

# Include this file immediately after Mk/copy.Mk in makefiles
# which are involved in building x86 version in Visual Studio
# environment.

# Include this file immediately after Mk/msys2.Mk in makefiles
# which are involved in building x86 version in Msys2 environments.

$(VR_SWIG_INTERFACE) : $(COPY_SWIG)
	$(DIRECTORY_VR_SWIG)
	cp -p $< $@


