#!/usr/bin/env bash


# how to setup this app ?
# 1, pip install --editable
# 2, export FLASK_APP=ethome
# 3, flask initdb
# 4, flask run

pip install --editable .


export FLASK_APP=ethome
export FLASK_DEBUG=True
flask run