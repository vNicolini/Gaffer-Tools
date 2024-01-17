@echo off
set SCRIPT_DIR=%cd%

setx GAFFER_TOOLS "%SCRIPT_DIR%" /M

timeout /T 2 /nobreak >nul

call set GAFFER_TOOLS=%SCRIPT_DIR%

if not defined GAFFER_STARTUP_PATHS (
    setx GAFFER_STARTUP_PATHS "%GAFFER_TOOLS%/startup" /M
) else (
    setx GAFFER_STARTUP_PATHS "%GAFFER_STARTUP_PATHS%;%GAFFER_TOOLS%/startup" /M
)

if not defined GAFFER_REFERENCE_PATHS (
    setx GAFFER_REFERENCE_PATHS "%GAFFER_TOOLS%/resources/references" /M
) else (
    setx GAFFER_REFERENCE_PATHS "%GAFFER_REFERENCE_PATHS%;%GAFFER_TOOLS%/resources/references" /M
)

rem check Gaffer paths are properly set up
set | findstr "GAFFER" | find /i "GAFFER"

PAUSE
