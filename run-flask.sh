#!/usr/bin/env bash

. /venv/bin/activate
pip install -r requirements.txt
flask run --host=0.0.0.0
