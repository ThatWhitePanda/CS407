#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
#export LOG_URL="http://127.0.0.1:8080/api/activities/"
#export LOG_URL="https://activitylogger-cli16.herokuapp.com/api/activities/"

#hw4--
export LOG_URL="http://0.0.0.0:5001/api/activities/"
flask run --host=0.0.0.0
