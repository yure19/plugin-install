#!/usr/bin/env bash

USAGE="Usage:
    # bash $BASH_SOURCE url username password"

if [ "$#" != "3" ]; then
    echo "error: missing some input values"
    echo "$USAGE"
    exit 3
fi

SCRIPT_DIRECTORY=$(dirname $0)

python3 -m venv "$SCRIPT_DIRECTORY/env"

source "$SCRIPT_DIRECTORY/env/bin/activate"

pip install -r "$SCRIPT_DIRECTORY/requirements"

MOZ_HEADLESS=1 python3 "$SCRIPT_DIRECTORY/install.py" "$1" "$2" "$3"

deactivate

rm -rf "$SCRIPT_DIRECTORY/env"

