# v3r0_sed_shared_c++11.Mk
# 'sed' '-f' arguments added to msys builds at c++11 standard.

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

# fastload_no_upper must be applied before msgini_restore_upper.
# The only way of locating the edit in fastload.cpp also edits
# msgini.cpp and msgini_restore_upper compensates for the unwanted
# edit.  These two edits tackle an application problem rather than
# a c++ toolchain problem.

SED_STDAFX_H_EDITS += -f sedCommands/extra_h_stdafx_c++11
SED_SRC_EDITS += -f sedCommands/make_pair \
                -f sedCommands/access_controller \
                -f sedCommands/i64_to_ll \
                -f sedCommands/comment_session \
                -f sedCommands/fastload_no_upper \
                -f sedCommands/msgini_restore_upper \
                -f sedCommands/resource_cpp_lockinfo
SED_INC_EDITS += -f sedCommands/resource_h_lockinfo

