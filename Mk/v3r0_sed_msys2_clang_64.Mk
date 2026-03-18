# Additional 'sed' '-f' arguments used in the msys2 clang 64 bit environment.

# The edits needed so far are not necessary in any 32-bit or the g++
# or VS environments.

# It is probably safe to do these in any environment.

SED_SRC_EDITS += \
                -f sedCommands/memcpy_pagebase_cpp

SED_INC_EDITS += \
                -f sedCommands/memcpy_pagebase_h
