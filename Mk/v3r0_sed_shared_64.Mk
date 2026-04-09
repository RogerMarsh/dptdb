# Additional 'sed' '-f' arguments used in at least one 64 bit environment.

# The edits needed so far look safe to do on 32 bit, but this is not done
# because it is not necessary.

# The rc_frecset_workaround change is derived from the 'cout' changes
# added and removed at previous two commits.

# rc_frecset_workaround should not be applied to 32 bit even if safe.
# It is wrong and is removed.

# trace_du_crash_x64 provides 'cout' statements surrounding the crash
# statement as close as practical: page_v.h has implementation.

SED_SRC_EDITS += -f sedCommands/bitmap3_cpp_01\
                 -f sedCommands/bitmap3_cpp_02\
                 -f sedCommands/bitmap3_cpp_03\
                 -f sedCommands/bitmap3_cpp_04\
                 -f sedCommands/bitmap3_cpp_05\
                 -f sedCommands/bitmap3_cpp_06\
                 -f sedCommands/bitmap3_cpp_07\
                 -f sedCommands/bitmap3_cpp_08\
                 -f sedCommands/bitmap3_cpp_09\
                 -f sedCommands/bitmap3_cpp_10\
                 -f sedCommands/bitmap3_cpp_11\
                 -f sedCommands/bitmap3_cpp_12\
                 -f sedCommands/bitmap3_cpp_13\
                 -f sedCommands/bitmap3_cpp_14\
                 -f sedCommands/bitmap3_cpp_15\
                 -f sedCommands/bitmap3_cpp_16\
                 -f sedCommands/bitmap3_cpp_17\
                 -f sedCommands/bitmap3_cpp_18\
                 -f sedCommands/bitmap3_cpp_19\
                 -f sedCommands/bitmap3_cpp_20\
                 -f sedCommands/bitmap3_cpp_21\
                 -f sedCommands/bitmap3_cpp_22\
                 -f sedCommands/bitmap3_cpp_23\
                 -f sedCommands/bitmap3_cpp_24\
                 -f sedCommands/bitmap3_cpp_25\
                 -f sedCommands/bitmap3_cpp_26\
                 -f sedCommands/bitmap3_cpp_27\
                 -f sedCommands/bitmap3_cpp_28\
                 -f sedCommands/bitmap3_cpp_29\
                 -f sedCommands/bitmap3_cpp_30\
                 -f sedCommands/bitmap3_cpp_31\
                 -f sedCommands/bitmap3_cpp_32\
                 -f sedCommands/bitmap3_cpp_33\
                 -f sedCommands/bitmap3_cpp_34\
                 -f sedCommands/bitmap3_cpp_35\
                 -f sedCommands/bitmap3_cpp_36\
                 -f sedCommands/bitmap3_cpp_37\
                 -f sedCommands/bitmap3_cpp_38\
                 -f sedCommands/bitmap3_cpp_39\
                 -f sedCommands/bitmap3_cpp_40\
                 -f sedCommands/bitmap3_cpp_41\
                 -f sedCommands/bitmap3_cpp_42\
                 -f sedCommands/bitmap3_cpp_43\
                 -f sedCommands/bitmap3_cpp_44

SED_INC_EDITS += -f sedCommands/bitmap3_h_01\
                 -f sedCommands/bitmap3_h_02\
                 -f sedCommands/bitmap3_h_03\
                 -f sedCommands/bitmap3_h_04\
                 -f sedCommands/bitmap3_h_05\
                 -f sedCommands/bitmap3_h_06\
                 -f sedCommands/bitmap3_h_07\
                 -f sedCommands/bitmap3_h_08\
                 -f sedCommands/bitmap3_h_09\
                 -f sedCommands/bitmap3_h_10\
                 -f sedCommands/bitmap3_h_11\
                 -f sedCommands/bitmap3_h_12\
                 -f sedCommands/bitmap3_h_13\
                 -f sedCommands/bitmap3_h_14\
                 -f sedCommands/bitmap3_h_15\
                 -f sedCommands/bitmap3_h_16\
                 -f sedCommands/bitmap3_h_17\
                 -f sedCommands/bitmap3_h_18\
                 -f sedCommands/bitmap3_h_19\
                 -f sedCommands/bitmap3_h_20\
                 -f sedCommands/bitmap3_h_21\
                 -f sedCommands/bitmap3_h_22\
                 -f sedCommands/bitmap3_h_23\
                 -f sedCommands/bitmap3_h_24
