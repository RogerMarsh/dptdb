# Additional 'sed' '-f' arguments for binary_function replacement as required.

SED_SRC_EDITS += \
                -f sedCommands/LeafInfoLessThanPredicate

SED_INC_EDITS += \
                -f sedCommands/NoCaseSortPredicate \
                -f sedCommands/FieldValueLessThanPredicate
