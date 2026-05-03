# v3r0_sed_resource_lockinfo.Mk
# Additional 'sed' '-f' arguments for operator in Resource::LockInfo.

SED_SRC_EDITS += -f sedCommands/resource_cpp_lockinfo

SED_INC_EDITS += -f sedCommands/resource_h_lockinfo
