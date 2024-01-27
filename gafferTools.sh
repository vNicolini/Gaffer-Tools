#!/bin/bash

# Get the current script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set GAFFER_TOOLS environment variable
export GAFFER_TOOLS=$SCRIPT_DIR

# Update GAFFER_STARTUP_PATHS variable
export GAFFER_STARTUP_PATHS=$GAFFER_STARTUP_PATHS:$GAFFER_TOOLS/startup

export GAFFER_REFERENCE_PATHS=$GAFFER_REFERENCE_PATHS:$GAFFER_TOOLS/resources/references

exe() { echo "\$ ${@/eval/}" ; "$@" ; }

# check gaffer paths are properly setup
exe eval "export |grep GAFFER"