# dpt.Mk
# Define extract directories for downloaded dpt version.

DPT = dpt
EXTRACT = $(DPT)/extract
EXTRACTED = $(EXTRACT)/$(DPT_VERSION)
SWIG_DPTAPI = dptapi
PYTHON_API_DLL = _$(SWIG_DPTAPI).pyd
CPP_TESTS = c++-tests
