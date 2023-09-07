# Additional 'sed' '-f' arguments used in at least one 64 bit environment.

# The edits needed so far look safe to do on 32 bit, but this is not done
# because it is not necessary.

# The rc_frecset_workaround change is derived from the 'cout' changes
# added and removed at previous two commits.

# rc_frecset_workaround should not be applied to 32 bit even if safe.

# trace_du_crash_x64 provides 'cout' statements surrounding the crash
# statement as close as practical: page_v.h has implementation.

SED_SRC_EDITS += \
                -f sedCommands/fn_lastrec \
                -f sedCommands/fn_temp \
                -f sedCommands/fn_bit_bit \
                -f sedCommands/fn_irelrec_nextbit \
                -f sedCommands/fp_irelrec_prevbit \
                -f sedCommands/fn_irelrec \
                -f sedCommands/rc_frecset_workaround \
                -f sedCommands/fn_singlerec

