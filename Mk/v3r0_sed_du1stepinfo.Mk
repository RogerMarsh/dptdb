# Additional 'sed' '-f' arguments for du1step info in 64 bit environments.

SED_SRC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedCpp

SED_INC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedH
