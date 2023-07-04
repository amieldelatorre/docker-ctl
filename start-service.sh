#!/bin/bash

python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
waitress-serve --host 0.0.0.0 --port 5000 --call app:create_app