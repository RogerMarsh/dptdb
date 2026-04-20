# extract-v3r06.Makefile
# Run in a Msys2 shell on Microsoft Windows.

# This file is derived from fetch.Makefile and adjusted.

# make -f extract-v3r06.Makefile
# extracts the DPT source from *.ZIP files,

# File containing the v3r06 source code.
SOURCE_V3R06 = DPT_V3R06_DBMS.ZIP

# Directories for the downloaded files.
# V3R06 is defined as $(BUILD)/v3r06 in the copy and build makefiles.

include Mk/v3r06_dpt.Mk

# For specific files which have to be renamed or moved to attic.
ATTIC = $(V3R06E)/Attic

# Licence.
DPT_LICENCE = licence.txt

# V3R06 does not have stdafx.cpp or stdafx.h files but the *.cpp and
# *.h files expect them.

V3R06E_STDAFX = $(V3R06E)/stdafx

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
COPY_SWIG = $(V3R06E)/$(SWIG_INTERFACE)

# Targets.

.PHONY : all copy clean

all : copy

copy : $(V3R06E) $(V3R06E_STDAFX) $(DPT_LICENCE) $(COPY_SWIG)

# The copy makefiles adjust the relevant '#include' directives.
# The relevant '#include' directives all refer to 'stdafx.h'.

# This comment is not relevant in this version of fetch.Makefile because
# no 'sed' commands need to be done.
# In 'sed' on FreeBSD '-I or -i may not be used with stdin'.
# OpenBSD and MinGW Msys accept "-i''" but getting a redundant backup is
# not too annoying.  (But first reading suggested option is not allowed!)
# (Moved from OpenBSD to FreeBSD when ready to test MinGW builds.)

# 'V3R06' source files reference 'stdafx.h' so put the one in 'HelloWorld'
# example in a more fitting location and rename to fit references.
# 'V3R06' is the local name for the stand-alone DBMS available on
# 'dptoolkit.com' until the site ceased to exist.

$(V3R06E_STDAFX) :
	mkdir $(V3R06E_STDAFX)
	cp -p $(V3R06E)/sample\ projects/HelloWorld*/StdAfx.h $@/stdafx.h
	cp -p $(V3R06E)/sample\ projects/HelloWorld*/StdAfx.cpp $@/stdafx.cpp

$(COPY_SWIG) :
	sed -e '/APIRoundedDouble_SetNum/s/_/\./g' \
	$(V3R06E)/sample\ projects/DPT\ with\ Python/$(SWIG_INTERFACE) > $@

$(DPT_LICENCE) :
	cp -p $(V3R06E)/$(DPT_LICENCE) .

$(DPT) :
	mkdir $(DPT)

$(EXTRACT) : $(DPT)
	mkdir $(EXTRACT)

$(V3R06E) : $(EXTRACT) $(SOURCE_V3R06)
	unzip -n -d $@ $(SOURCE_V3R06)

clean :
	-rm $(DPT_LICENCE)
	-rm -rf $(DPT)

# Some files, no examples in V3R0, are redundant and must be removed from
# the scope of pattern rules.

# Provide an attic for these files.

# The 'attic' rules present in the dpt-makefile version of this makefile
# are removed.

