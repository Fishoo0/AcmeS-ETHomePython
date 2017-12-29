import json
import os

from flask import Flask, request, json, jsonify

from ethome.schema.db import init_db, close_db
from ethome.src.json import jsonutils
from ethome.src.login.login import Login

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'ethome.db'),
    DEBUG=True,
    SECRET_KEY='haohaoxuexi',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('ETHOME_SETTINGS', silent=True)


@app.cli.command('init_db')
def init_command():
    init_db()


@app.teardown_appcontext
def release_db(error):
    """ do when app is down"""
    close_db()


# Bellowing are urls

@app.route('/')
def welcome():
    return jsonutils.get_success_msg('Welcome to ETHome!')


def check_params(user_name, user_password='silent'):
    if user_name is None:
        return jsonify(jsonutils.get_error_msg('Invalid user_name'))
    if user_password is None or user_password is '':
        return jsonify(jsonutils.get_error_msg('Invalid user_password'))
    return None


@app.route('/register', methods=['POST'])
def register():
    content = request.get_json()
    user_name = content.get('user_name')
    user_password = content.get('user_password')
    check_result = check_params(user_name, user_password)
    if check_result is not None:
        return check_result
    result = Login.register(user_name, user_password)
    if result is not None:
        return jsonify(jsonutils.get_error_msg(result))
    return jsonify(jsonutils.get_success_msg('Register successfully!'))


@app.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    user_name = content.get('user_name')
    user_password = content.get('user_password')
    check_result = check_params(user_name, user_password)
    if check_result is not None:
        return check_result
    result = Login.login(user_name, user_password)
    if result is not None:
        return jsonify(jsonutils.get_error_msg(result))
    return jsonify(jsonutils.get_success_msg('Login successfully!'))


@app.route('/logout', methods=['POST'])
def logout():
    content = request.get_json()
    user_name = content.get('user_name')
    check_result = check_params(user_name)
    if check_result is not None:
        return check_result
    result = Login.logout(user_name)
    if result is not None:
        return jsonify(jsonutils.get_error_msg(result))
    return jsonify(jsonutils.get_success_msg('Logout successfully!'))


@app.route('/get_home', methods=['GET', 'POST'])
def get_home():
    return json.loads({'code': 0, 'message': '', 'data': [{'value': 'First item'}]})
