SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export GAFFER_TOOLS=$SCRIPT_DIR

export GAFFER_STARTUP_PATHS=$AFFER_STARTUP_PATHS;$GAFFER_TOOLS/startup

export GAFFER_REFERENCE_PATHS=$GAFFER_REFERENCE_PATHS;$GAFFER_TOOLS/resources/references

# check gaffer paths are properly setup
exe eval "export |grep GAFFER"

read -n 1 -s -r -p "Press any key to continue..."
