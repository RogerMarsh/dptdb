# Additional 'sed' '-f' arguments used in at least one 64 bit environment.

# The edits needed so far look safe to do on 32 bit, but this is not done
# because it is not necessary.

# The rc_frecset_irelrec and rc_frecset_relrec changes use std::cout so
# '#include <iostream> must be added near top of frecset.cpp file.

# However there is no way of adding this just to frecset.cpp with 'sed'
# because the pattern match must include newline characters.

# So that edit MUST be done manually AFTER the 'copy' and BEFORE the
# 'build' for Visual Studio builds.

# The build with these edits CANNOT be done on Msys2 with 'sed' because
# there is no separation between 'copy' and 'build'.  The edits HAVE to
# be done manually on the 'extract' of frecset.cpp before running the
# build on Msys2.

SED_SRC_EDITS += \
                -f sedCommands/fn_lastrec \
                -f sedCommands/fn_temp \
                -f sedCommands/fn_bit_bit \
                -f sedCommands/fn_irelrec_nextbit \
                -f sedCommands/fp_irelrec_prevbit \
                -f sedCommands/fn_irelrec \
                -f sedCommands/fn_singlerec \
                -f sedCommands/rc_frecset_irelrec \
                -f sedCommands/rc_frecset_relrec

