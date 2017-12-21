#!/usr/bin/env bash


# how to setup this app ?
# 1, pip3 install --editable .
# 2, export FLASK_APP=ethome
# 3, flask init_db
# 4, flask run



export FLASK_APP=ethome
export FLASK_DEBUG=True
flask run