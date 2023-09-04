# Additional 'sed' '-f' arguments used in Msys2 64 bit environment.

# The edits needed so far are not necessary in msys2 32-bit or any vs
# environment.  The gcc compiler gives an error which states what is
# wrong and suggests '-fpermissive' which may be the thing to do if
# these are the only ones because none of the methods are called
# within the DPT code or are diagnostic tools.  The 64-bit vs compiler
# gives a warning for most of the instances but no errors.

# fperm_winutil_addr is editing the result of a previous edit: another
# environment must need '(unsigned long)addr'.

SED_SRC_EDITS += \
                -f sedCommands/fperm_dataconv \
                -f sedCommands/fperm_findwork \
                -f sedCommands/fperm_winutil_gul \
                -f sedCommands/fperm_winutil_addr

SEDAPI_SRC_EDITS += \
                -f sedCommands/fperm_findspec_api
