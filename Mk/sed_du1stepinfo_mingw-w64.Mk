# sed_du1stepinfo_mingw-w64.Mk
# Extra 'sed' '-f' arguments for du1step info in 64 bit environments.
# The command for source directory edits in BSD and Linux environments
# has to represent newline as '\n'.
# The 'what you see is what you get' style for the Msys2 environment is
# not acceptable in the substitution string here.
# See ./sed_du1stepinfo.Mk and ../sedCommands/DU1StepInfoIsInitializedCpp
# files.

SED_SRC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedCpp_mingw-w64

SED_INC_EDITS += \
                -f sedCommands/DU1StepInfoIsInitializedH
