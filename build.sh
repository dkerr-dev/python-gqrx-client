#!/bin/sh

(
    # Activate the python virtual environment
    python3 -m venv .venv
    . .venv/bin/activate
    pip install --upgrade -r requirements.txt

    # Build the documentation
    (
        cd docs
        make html
    )

    # Build the library
    (
        python3 -m pip install --upgrade build
        python3 -m build
    )

)
