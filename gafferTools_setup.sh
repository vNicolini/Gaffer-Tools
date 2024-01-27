#!/bin/bash

# Get the current script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set GAFFER_TOOLS environment variable
echo "export GAFFER_TOOLS=\"$SCRIPT_DIR\"" >> ~/.bashrc

# Update GAFFER_STARTUP_PATHS variable
if [ -z "$GAFFER_STARTUP_PATHS" ]; then
    echo "export GAFFER_STARTUP_PATHS=\"$SCRIPT_DIR/startup\"" >> ~/.bashrc
else
    echo "export GAFFER_STARTUP_PATHS=\"$GAFFER_STARTUP_PATHS:$SCRIPT_DIR/startup\"" >> ~/.bashrc
fi

# Update GAFFER_REFERENCE_PATHS variable
if [ -z "$GAFFER_REFERENCE_PATHS" ]; then
    echo "export GAFFER_REFERENCE_PATHS=\"$SCRIPT_DIR/resources/references\"" >> ~/.bashrc
else
    echo "export GAFFER_REFERENCE_PATHS=\"$GAFFER_REFERENCE_PATHS:$SCRIPT_DIR/resources/references\"" >> ~/.bashrc
fi

# Source the updated .bashrc to apply changes
source ~/.bashrc

exe() { echo "\$ ${@/eval/}" ; "$@" ; }

# check gaffer paths are properly setup
exe eval "export |grep GAFFER"

# Pause for user input
read -n 1 -s -r -p "Press any key to continue..."