#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=development
export SLEEP_TIME=5

flask run --host=0.0.0.0
