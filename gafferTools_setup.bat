@echo off

@for /f "delims=" %%I in ('cd /d "%~dp0" && echo %cd%') do set SCRIPT_DIR=%%I

setx GAFFER_TOOLS "%SCRIPT_DIR%"

setx GAFFER_STARTUP_PATHS=%GAFFER_STARTUP_PATHS%;%GAFFER_TOOLS%/startup

setx GAFFER_REFERENCE_PATHS=%GAFFER_REFERENCE_PATHS%;%GAFFER_TOOLS/resources/references

rem check gaffer paths are properly setup
set | findstr "GAFFER" | find /i "GAFFER"

PAUSE