# 'sed' '-f' arguments used in at least one environment.

# In MinGW (now sourceforge.net/projects/mingw) the 'sed' arguments were
# rather fragmented depending on age of mingw-get-setup.exe and update
# state controlled by libexec/mingw-get/guimain.exe.

# In msys64 (now mingw-w64.org), and in the past often referred to as
# msys2, system management seems simpler: there is less scope for old
# versions in parallel and the sed arguments, so far, apply to all c++
# standards.

# The range of standards available in Visual Studio Developer Command
# Prompt versions is less, but all here apply to the successful build
# in the 2017 version at c++14.

# There seems to be a difference of opinion between msys2 and vs on one
# point in the c++ standards which leads to v3r0 building successfully
# at all c++ standards on msys2 but only on vs2017 at c++14 in Visual
# Studio Developer Command Prompt.

# The name 'extra_h_stdafx_c++14' in the SED_STDAFX_H_EDITS definition
# refers to the need for this edit at c++14 in one of the later MinGW
# installations, and will likely be a bit baffling in the msys2 and vs
# environments in future.  'extra_h_stdafx_c++14' was different from
# 'extra_h_stdafx_c++98' at one time: but this was relevant only in the
# MinGW environments.

# MinGW worked with the Python built for Microsoft Windows but Msys2
# provides it's own port of Python which runs in the Msys2 environment
# on Microsoft Windows.  The Visual Studio Developer Command Prompt
# option was not available until yyyy.  MinGW was the superior solution
# to building dptdb until it become impossible to run a Python interface
# to DPT built in the MinGW environment.

SED_STDAFX_H_EDITS = -f sedCommands/extra_h_stdafx_c++14
SED_SRC_EDITS = -f sedCommands/back_to_forward_slant \
                -f sedCommands/make_pair \
                -f sedCommands/access_controller \
                -f sedCommands/i64_to_ll \
                -f sedCommands/comment_session \
                -f sedCommands/ord_comp_ptr_int
SED_INC_EDITS = -f sedCommands/back_to_forward_slant
SEDAPI_SRC_EDITS = -f sedCommands/back_to_forward_slant
SEDAPI_INC_EDITS = -f sedCommands/back_to_forward_slant
SED_STDAFX_CPP_EDITS = -f sedCommands/back_to_forward_slant

