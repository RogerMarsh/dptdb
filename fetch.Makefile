# Download DPT source from copies of zip files from dptoolkit website
# before it was shut.

# Currently if a sequence of n, n > 2, invocations of this makefile is
# done when just the zip files exist, the first one does the extractions
# without prompts, the second prompts for overwrite permission, and the
# rest say 'nothing to be done'.

# Download site.
DOWNLOAD_URL = http://solentware.co.uk/files/

# Files at download site.
# Downloads, or copies obtained otherwise, are kept as siblings of the
# directory containing fetch.Makefile.
# V3R0E is not appropriate for these two names because the distinction
# is versions of DPT DBMS, not reference to extract, copy and build.
# There is a DPT_V3R06_DBMS.ZIP file for example.
SOURCE_V3R0 = DPT_V3R0_DBMS.ZIP
DOCUMENTATION_V3R0 = DPT_V3R0_DOCS.ZIP

# Directories for the downloaded files.
# V3R0 is defined as $(BUILD)/v3r0 in the copy and build makefiles.

include Mk/v3r0_dpt.Mk

DOCS_V3R0E = $(EXTRACT)/docs_v3r0

# For specific files which have to be renamed or moved to attic.
ATTIC = $(V3R0E)/Attic

# Licence.
DPT_LICENCE = licence.txt

# V3R0 download does not have stdafx.cpp or stdafx.h files but the *.cpp
# and *.h files expect them.

V3R0E_STDAFX = $(V3R0E)/stdafx

# The *.i file defining the SWIG interface.
SWIG_INTERFACE = dptapi_python.i
COPY_SWIG = $(V3R0E)/$(SWIG_INTERFACE)

# Targets.

.PHONY : all copy clean

all : copy

copy : $(DOCS_V3R0E) $(V3R0E) $(V3R0E_STDAFX) $(DPT_LICENCE) $(COPY_SWIG)

# The copy makefiles adjust the relevant '#include' directives.
# The relevant '#include' directives all refer to 'stdafx.h'.

# This comment is not relevant in this version of fetch.Makefile because
# no 'sed' commands need to be done.
# In 'sed' on FreeBSD '-I or -i may not be used with stdin'.
# OpenBSD and MinGW Msys accept "-i''" but getting a redundant backup is
# not too annoying.  (But first reading suggested option is not allowed!)
# (Moved from OpenBSD to FreeBSD when ready to test MinGW builds.)

# 'V3R0' source files reference 'stdafx.h' so put the one in 'HelloWorld'
# example in a more fitting location and rename to fit references.
# 'V3R0' is the local name for the stand-alone DBMS available on
# 'dptoolkit.com' until the site ceased to exist.  DBMS is best used as
# the name of the 'V3R06' product, a later version broken in recent
# compliers, copied from
# https://drive.google.com/drive/folders/0B1GLdfqdwpNQUVE0ekFWalEtVHM0

$(V3R0E_STDAFX) :
	mkdir $(V3R0E_STDAFX)
	cp -p $(V3R0E)/sample\ projects/HelloWorld*/StdAfx.h $@/stdafx.h
	cp -p $(V3R0E)/sample\ projects/HelloWorld*/StdAfx.cpp $@/stdafx.cpp

# Between swig-4.0.1 and swig-4.1.1 the <class>_<static method>()
# construct became unsupported by swig.
# The <class>.<static method>() construct must be used instead, and is
# supported at swig-4.0.1 and swig-2.0.8 too (so likely ok always).

$(COPY_SWIG) :
	sed -e '/APIRoundedDouble_SetNum/s/_/\./g' \
	$(V3R0E)/sample\ projects/DPT\ with\ Python/$(SWIG_INTERFACE) > $@

$(DPT_LICENCE) :
	cp -p $(V3R0E)/$(DPT_LICENCE) .

$(DPT) :
	mkdir $(DPT)

$(EXTRACT) : $(DPT)
	mkdir $(EXTRACT)

$(V3R0E) : $(EXTRACT) $(SOURCE_V3R0)
	unzip -n -d $@ $(SOURCE_V3R0)

$(DOCS_V3R0E) : $(EXTRACT) $(DOCUMENTATION_V3R0)
	unzip -n -d $@ $(DOCUMENTATION_V3R0)

clean :
	-rm $(DPT_LICENCE)
	-rm -rf $(DPT)

$(DOCUMENTATION_V3R0) :
	curl --output $@ $(DOWNLOAD_URL)$(DOCUMENTATION_V3R0)

$(SOURCE_V3R0) :
	curl --output $@ $(DOWNLOAD_URL)$(SOURCE_V3R0)

# Some files, no examples in V3R0, are redundant and must be removed from
# the scope of pattern rules.

# Provide an attic for these files.

# The 'attic' rules present in the dpt-makefile version of this makefile
# are removed.

