# extract_from_zip.Mk

# Include this file in a makefile that defines these variables:
# DIRECTORY_EXTRACT
# DIRECTORY_EXTRACTED
# DIRECTORY_EXTRACTED_STDAFX
# DOCS_EXTRACTED
# DOCUMENTATION_ZIP
# DPT_LICENCE
# EXTRACTED
# EXTRACTED_STDAFX
# COPY_SWIG
# SOURCE_ZIP
# SWIG_INTERFACE

# 'V3R0' source files reference 'stdafx.h' so put the one in 'HelloWorld'
# example in a more fitting location and rename to fit references.
# 'V3R0' is the local name for the stand-alone DBMS available on
# 'dptoolkit.com' until the site ceased to exist.  DBMS is best used as
# the name of the 'V3R06' product, a later version broken in recent
# compliers, copied from
# https://drive.google.com/drive/folders/0B1GLdfqdwpNQUVE0ekFWalEtVHM0

# 'cp -p' in these rules leads to repeating actions if 'copy' target
# is re-used.

$(EXTRACTED_STDAFX)/stdafx.h : $(EXTRACTED)/$(DPT_LICENCE)
	$(DIRECTORY_EXTRACTED_STDAFX)
	cp $(EXTRACTED)/sample\ projects/HelloWorld*/StdAfx.h $@

$(EXTRACTED_STDAFX)/stdafx.cpp : $(EXTRACTED)/$(DPT_LICENCE)
	$(DIRECTORY_EXTRACTED_STDAFX)
	cp $(EXTRACTED)/sample\ projects/HelloWorld*/StdAfx.cpp $@

# Between swig-4.0.1 and swig-4.1.1 the <class>_<static method>()
# construct became unsupported by swig.
# The <class>.<static method>() construct must be used instead, and is
# supported at swig-4.0.1 and swig-2.0.8 too (so likely ok always).

$(COPY_SWIG) : $(EXTRACTED_STDAFX)/stdafx.h $(EXTRACTED_STDAFX)/stdafx.cpp
	$(DIRECTORY_EXTRACTED)
	sed -e '/APIRoundedDouble_SetNum/s/_/\./g' \
	$(EXTRACTED)/sample\ projects/DPT\ with\ Python/$(SWIG_INTERFACE) > $@

$(EXTRACTED)/$(DPT_LICENCE) : $(SOURCE_ZIP) $(DOCS_EXTRACTED)/_Doc_Read_Me.txt
	$(DIRECTORY_EXTRACT)
	unzip -n -d $(EXTRACTED) $<

$(DOCS_EXTRACTED)/_Doc_Read_Me.txt : $(DOCUMENTATION_ZIP)
	$(DIRECTORY_EXTRACT)
	unzip -n -d $(DOCS_EXTRACTED) $(DOCUMENTATION_ZIP)
