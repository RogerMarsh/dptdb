# Additional 'sed' '-f' arguments used in at least one 64 bit environment.

# The edits needed so far look safe to do on 32 bit, but this is not done
# because it is not necessary.

# rc_bitmap added because it avoids 'Bit subscript out of mapped range'
# RuntimeError on x64 environment without apparent bad effects.  It occurs
# in a very specific circumstance where application logic and available
# evidence suggest the problem is NOT what the application is trying to
# do, but prior setup of the constant which decides validity of action.
# (The edited statement would likely be coded as an assert in Python.)

SED_SRC_EDITS += \
                -f sedCommands/fn_lastrec \
                -f sedCommands/fn_temp \
                -f sedCommands/fn_bit_bit \
                -f sedCommands/fn_irelrec_nextbit \
                -f sedCommands/fp_irelrec_prevbit \
                -f sedCommands/fn_irelrec \
                -f sedCommands/fn_singlerec

SED_INC_EDITS += \
                -f sedCommands/rc_bitmap
