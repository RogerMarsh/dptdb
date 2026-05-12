# mingw-w64_build.Mk
# Compiler settings.

CXX = $(PATH_TO_CXX)$(COMPILER)
DEFOPTS = $(DEFINES) $(OPTIONS)
CXXEXTRA = -D_BBDBAPI -std=$(CPPSTANDARD)
DPT_LDFLAGS = -shared

# Build includes (-I) options for compiler.

VR_INCLUDE = -I$(VR_INC) -I$(VR_STDAFX)
VR_API_INCLUDE = -I$(VR_INC) -I$(VR_API_INC) -I$(VR_STDAFX)
DPTAFX_INCLUDE = -I$(VR_INC) -I$(VR_STDAFX)

# Object directories.

DIRECTORY_VR_OBJECT = @mkdir -p $(VR_OBJECT)
DIRECTORY_VR_STDAFX_OBJECT = @mkdir -p $(VR_STDAFX_OBJECT)
DIRECTORY_VR_API_OBJECT = @mkdir -p $(VR_API_OBJECT)
DIRECTORY_VR_SWIG_OBJECT = @mkdir -p $(VR_SWIG_OBJECT)

# Pattern rules DPT C++.

$(VR_OBJECT)/%.o : $(VR_SRC)/%.cpp
	$(DIRECTORY_VR_OBJECT)
	$(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(VR_INCLUDE) $(DEFOPTS) -o $@ $<

$(VR_API_OBJECT)/%.o : $(VR_API_SRC)/%.cpp
	$(DIRECTORY_VR_API_OBJECT)
	$(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(VR_API_INCLUDE) $(DEFOPTS) -o $@ $<

$(VR_STDAFX_OBJECT)/%.o : $(VR_STDAFX)/%.cpp
	$(DIRECTORY_VR_STDAFX_OBJECT)
	$(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(DPTAFX_INCLUDE) $(DEFOPTS) -o $@ $<

# Object file names.

OBJS = $(SED_NAMES:%=$(VR_OBJECT)/%.o)

API_OBJS = $(SED_API_NAMES:%=$(VR_API_OBJECT)/%.o)

AFX_OBJS = $(SED_AFX_NAMES:%=$(VR_STDAFX_OBJECT)/%.o)

OBJECT_FILES = $(OBJS) $(AFX_OBJS) $(API_OBJS)

$(OBJECT_FILES) : $(VR_STDAFX)/stdafx.h $(INCS) $(API_INCS)

# Copy package template directory for build and local install.

# In Msys2 MINGW32 terminal the commented version, copy then sed
# in-place, does the edit but then sed fails claiming it is unable
# to read a file. So sed then copy without overwrite.
# Never got to see if same happens in Msys2 MINGW64 terminal.

$(VR_PACKAGE) : package-template
	-mkdir $@
	sed -e '/"invalid"/s/invalid/$(DPT_DPTDB_VERSION)/g' $</pyproject.toml > $@/pyproject.toml
	cp -nrp $</* $@/
#	cp -rp $</* $@/
#	sed -i '' -e '/"invalid"/s/invalid/$(DPT_DPTDB_VERSION)/g' $@/pyproject.toml

# SWIG wrapper rules.
# Comments on 'sed' edits for the MinGW (sourceforge.net/projects/mingw),
# not MinGW-w64 (mingw-w64.org), toolchain are removed compared with the
# replaced dptMakefile.
# sourceforge.net/projects/mingw refers to osdn.net/projects/mingw which
# does not exist at 2023-08-09, and mingw-w64.org distinguishes itself from
# mingw.org, an earlier home for sourceforge.net/projects/mingw I believe.
# See dptdb versions earlier than 0.9 if it seems they might be relevant.

# There is a clash between MinGW and Python on _hypot and hypot for cmath.
# www.freelists.org/post/nuitka-dev/error-hypot-has-not-been-declared,2 and
# stackoverflow.com/questions/10660524/error-building-boost-...-gcc-4-7-0...
# are two of many threads suggesting two possible workarounds.  (Why is
# this project not affected until after MinGW-5.3.0 given Boost's 4.7.0
# experience?) -D_hypot=hypot added to Swig wrapper build.

# At 2023-08-09 the swig workaround for hypot clash was seen in generated
# dptapi_python_wrap.cxx so the -D_hypot=hypot is removed.

# Python distribution settings.

PYTHON_NAME = Python
SWIG_PYTHON = python
PYTHON_MAJOR = 3
PYTHON_MINOR = 14
PYTHON_MAJOR_MINOR = $(PYTHON_MAJOR)$(PYTHON_MINOR)
PYTHON_VERSION = $(PYTHON_MAJOR_MINOR)
PYTHON_TAG = cp$(PYTHON_MAJOR)$(PYTHON_MINOR)
ABI_TAG = cp$(PYTHON_MAJOR)$(PYTHON_MINOR)
DPT_DBMS_OBJECT_SWIG_PYTHON = $(DPT_DBMS_OBJECT_SWIG)/$(PYTHON_VERSION)

PYTHON_HEADER = $(PYTHON_NAME).h
PYTHON_VERSION_PATH = Programs/$(PYTHON_NAME)/$(PYTHON_NAME)$(PYTHON_VERSION)
WINE_APPDATA = ../.wine/drive_c/users/$(USER)/AppData/Local
PYTHON_INCLUDE = $(WINE_APPDATA)/$(PYTHON_VERSION_PATH)/include
PYTHON_LIBS_DIRECTORY = $(WINE_APPDATA)/$(PYTHON_VERSION_PATH)/libs
PYTHON_LIBRARY = $(SWIG_PYTHON)$(PYTHON_MAJOR_MINOR)

WRAP_CXX = $(VR_SWIG)/$(SWIG_DPTAPI)_$(SWIG_PYTHON)_wrap.cxx
WRAP_O = $(VR_SWIG_OBJECT)/$(SWIG_DPTAPI)_$(SWIG_PYTHON)_wrap.o

$(WRAP_CXX) : $(VR_PACKAGE) $(VR_SWIG_INTERFACE)
	$(WINE) $(SWIG_COMMAND) -c++ -$(SWIG_PYTHON) -o $@ -outdir $(VR_PACKAGE_DPTDB) -I$(VR_API_INC) $(VR_SWIG_INTERFACE)

$(WRAP_O) : $(WRAP_CXX)
	$(DIRECTORY_VR_SWIG_OBJECT)
	$(CXX) -c $(CXXEXTRA) $(CXXFLAGS) -I$(VR_API_INC) -I$(VR_INC) -I$(PYTHON_INCLUDE) $(DEFOPTS) -o $@ $(WRAP_CXX)

# The .pyd file built from SWIG.

$(VR_PACKAGE_DPTDB)/$(PYTHON_API_DLL) : $(OBJECT_FILES) $(WRAP_O)
	$(CXX) $(DPT_LDFLAGS) -o $@ $(WRAP_O) $(API_OBJS) $(OBJS) -l$(PYTHON_LIBRARY) -L$(PYTHON_LIBS_DIRECTORY)

wrapper : $(VR_PACKAGE_DPTDB)/$(PYTHON_API_DLL)
	$(WINE) python -m build --wheel --no-isolation $(VR_PACKAGE)
	$(WINE) python -m wheel tags --python-tag=$(PYTHON_TAG) --abi-tag=$(ABI_TAG) --platform-tag=$(PLATFORM_TAG) --remove $(VR_PACKAGE)/dist/dpt3_0_dptdb-$(DPT_DPTDB_VERSION)-py3-none-any.whl

local-install : wrapper
	$(WINE) python -m pip install --user --no-index --find-links $(VR_PACKAGE)/dist dpt3.0_dptdb

# Build tests with c++ in a mingw-w64 32-bit or 64-bit environment.

# Test file names.

TEST_NAMES = $(basename $(notdir $(wildcard c++-tests/source/*.cpp)))

TEST_OBJS = $(TEST_NAMES:%=$(VR_TESTS)/%.o)

TEST_EXES = $(TEST_NAMES:%=$(VR_TESTS)/%.exe)

# Includes for c++ builds of tests.

VR_TESTS_INCLUDE = -I$(VR_INC) -I$(VR_API_INC)

# Pattern rules C++ tests.

$(VR_TESTS)/%.o : c++-tests/source/%.cpp
	$(DIRECTORY_VR_TESTS)
	$(CXX) -c $(CXXEXTRA) $(CXXFLAGS) $(VR_TESTS_INCLUDE) $(DEFOPTS) -o $@ $<

$(VR_TESTS)/%.exe : $(VR_TESTS)/%.o
	$(DIRECTORY_VR_TESTS)
	$(CXX) $(CXXEXTRA) $(CXXFLAGS) $(VR_TESTS_INCLUDE) $(DEFOPTS) -o $@ $< $(API_OBJS) $(OBJS)

# Use tests target if a test module has changed.

tests : copy-all $(TEST_EXES) $(VR_TESTS)/$(PARMS_DU_SINGLE) $(VR_TESTS)/$(PARMS_NORMAL) $(VR_TESTS)/$(PARMS_DU_MULTI)

$(TEST_EXES) : $(OBJECT_FILES)

