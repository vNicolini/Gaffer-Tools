@echo off

:: Sets the variables to be passed on to your Gaffer's wrapper

set SCRIPT_DIR=%~dp0

set GAFFER_TOOLS=%SCRIPT_DIR%

if "%GAFFER_STARTUP_PATHS%"=="" (
    set GAFFER_STARTUP_PATHS=%GAFFER_TOOLS%startup
) else (
    set GAFFER_STARTUP_PATHS=%GAFFER_STARTUP_PATHS%;%GAFFER_TOOLS%startup
)

if "%GAFFER_REFERENCE_PATHS%"=="" (
    set GAFFER_REFERENCE_PATHS=%GAFFER_TOOLS%resources\references
) else (
    set GAFFER_REFERENCE_PATHS=%GAFFER_REFERENCE_PATHS%;%GAFFER_TOOLS%resources\references
)
