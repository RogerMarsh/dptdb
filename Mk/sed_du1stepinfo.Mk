# sed_du1stepinfo.Mk
# Extra 'sed' '-f' arguments for du1step info in 64 bit environments.
# The 'what you see is what you get' style in the source directory
# edit was seen to work in Msys2 environment before it was seen to
# not work in BSD and Linux environments.  The '\n' style is not
# copied from ../sedCommands/DU1StepInfoIsInitializedCpp_mingw-w64
# because it is less readable by eye, even though it works here.

SED_SRC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedCpp

SED_INC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedH
