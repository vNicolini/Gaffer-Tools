@echo off

set SCRIPT_DIR=%cd%

setx GAFFER_TOOLS "%SCRIPT_DIR%"

if not defined GAFFER_STARTUP_PATHS (
    setx GAFFER_STARTUP_PATHS "%GAFFER_TOOLS%/startup"
) else (
    setx GAFFER_STARTUP_PATHS "%GAFFER_STARTUP_PATHS%;%GAFFER_TOOLS%/startup"
)

if not defined GAFFER_REFERENCE_PATHS (
    setx GAFFER_REFERENCE_PATHS "%GAFFER_TOOLS%/resources/references"
) else (
    setx GAFFER_REFERENCE_PATHS "%GAFFER_REFERENCE_PATHS%;%GAFFER_TOOLS%/resources/references"
)

rem check Gaffer paths are properly set up
set | findstr "GAFFER" | find /i "GAFFER"

PAUSE
