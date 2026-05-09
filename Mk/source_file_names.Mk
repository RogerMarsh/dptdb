# source_file_names.Mk

# Populate SOURCE_FILES with names of *.cpp and *.h files extracted
# from the DPT DBMS zip file.

# Include this file in a makefile that defines these variables:
# VR_DIRECTORY
# EXTRACTED

# The first run of a makefile intended to create a copy, probably
# edited as well, of the source files will extract the files but not
# do the copy.

# The second run will not do the extract, but will do the copy.

# Later runs will do nothing, assuming none of the files created in
# the first two runs have been deleted or modified.

# DPT extract and build folders.

VR_SRC = $(VR_DIRECTORY)/source
VR_INC = $(VR_DIRECTORY)/include
VR_API_SRC = $(VR_SRC)/dbapi
VR_API_INC = $(VR_INC)/dbapi
VR_STDAFX = $(VR_DIRECTORY)/stdafx
SED_SRC = $(EXTRACTED)/source
SED_INC = $(EXTRACTED)/include
SED_API_SRC = $(SED_SRC)/dbapi
SED_API_INC = $(SED_INC)/dbapi
SED_STDAFX = $(EXTRACTED)/stdafx

DIRECTORY_VR_API_SRC = @mkdir -p $(VR_API_SRC)
DIRECTORY_VR_SRC = @mkdir -p $(VR_SRC)
DIRECTORY_VR_API_INC = @mkdir -p $(VR_API_INC)
DIRECTORY_VR_INC = @mkdir -p $(VR_INC)
DIRECTORY_VR_STDAFX = @mkdir -p $(VR_STDAFX)
DIRECTORY_VR_SWIG = @mkdir -p $(VR_SWIG)
DIRECTORY_VR = @mkdir -p $(VR_DIRECTORY)

SED_NAMES = $(basename $(notdir $(wildcard $(SED_SRC)/*.cpp)))

SED_API_NAMES = $(basename $(notdir $(wildcard $(SED_API_SRC)/*.cpp)))

SED_INC_NAMES = $(basename $(notdir $(wildcard $(SED_INC)/*.h)))

SED_API_INC_NAMES = $(basename $(notdir $(wildcard $(SED_API_INC)/*.h)))

SED_AFX_NAMES = $(basename $(notdir $(wildcard $(SED_STDAFX)/*.cpp)))

SRCS = $(SED_NAMES:%=$(VR_SRC)/%.cpp)

API_SRCS = $(SED_API_NAMES:%=$(VR_API_SRC)/%.cpp)

INCS = $(SED_INC_NAMES:%=$(VR_INC)/%.h)

API_INCS = $(SED_API_INC_NAMES:%=$(VR_API_INC)/%.h)

AFX_SRCS = $(SED_AFX_NAMES:%=$(VR_STDAFX)/%.cpp)

AFX_INCS = $(SED_AFX_NAMES:%=$(VR_STDAFX)/%.h)

SOURCE_FILES = $(SRCS) $(INCS) $(API_SRCS) $(API_INCS) $(AFX_SRCS) $(AFX_INCS)

