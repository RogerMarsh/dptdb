# Additional 'sed' '-f' arguments used in at least one 64 bit environment.

# The edits needed so far look safe to do on 32 bit, but this is not done
# because it is not necessary.

# The rc_frecset_workaround change is derived from the 'cout' changes
# added and removed at previous two commits.

# rc_frecset_workaround should not be applied to 32 bit even if safe.

# resource_cpp_lockinfo and resource_h_lockinfo are probably safe on 32-bit
# but should be applied only if a clang 32-bit build becomes necessary or
# desirable and requires them.

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
                -f sedCommands/fn_singlerec \
                -f sedCommands/resource_cpp_lockinfo

SED_INC_EDITS += \
                -f sedCommands/resource_h_lockinfo

