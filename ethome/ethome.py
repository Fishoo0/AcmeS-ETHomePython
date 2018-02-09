import json
import os
import urllib.request

from flask import Flask, request, json

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


def check_params(user_name, user_password=None, check_password=True):
    if user_name is None:
        return jsonutils.get_error_msg('Invalid user_name')
    if (user_password is None or user_password is '') and check_password:
        return jsonutils.get_error_msg('Invalid user_password')
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
        return jsonutils.get_error_msg(result)
    return jsonutils.get_success_msg('Register successfully!')


@app.route('/login', methods=['POST'])
def login():
    print("login")
    content = request.get_json()
    print(content)
    user_name = content.get('user_name')
    user_password = content.get('user_password')
    check_result = check_params(user_name, user_password, check_password=False)
    if check_result is not None:
        return check_result
    result = Login.login(user_name, user_password)
    if result is not None:
        return jsonutils.get_error_msg(result)
    return jsonutils.get_success_msg('Login successfully!')


@app.route('/logout', methods=['POST'])
def logout():
    content = request.get_json()
    user_name = content.get('user_name')
    check_result = check_params(user_name, check_password=False)
    if check_result is not None:
        return check_result
    result = Login.logout(user_name)
    if result is not None:
        return jsonutils.get_error_msg(result)
    return jsonutils.get_success_msg('Logout successfully!', data=json.dumps({'user_name': user_name}))


@app.route('/get_home', methods=['GET', 'POST'])
def get_home():
    value = json.dumps({'code': 0, 'message': '', 'data': [{'value': 'First item'}]})
    return value


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    print("categories")
    url = 'https://api.avgle.com/v1/categories'
    response = json.loads(urllib.request.urlopen(url).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['categories']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)


@app.route('/collections', methods=['GET', 'POST'])
def avgle_collections():
    print("avgle_collections")
    url = 'https://api.avgle.com/v1/collections/{}?limit={}'
    page = 0
    limit = 2
    response = json.loads(
        urllib.request.urlopen(url.format(page, limit)).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['collections']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)


@app.route('/videos', methods=['GET', 'POST'])
def avgle_videos():
    print("avgle_videos")
    url = 'https://api.avgle.com/v1/videos/{}?limit={}'
    page = 0
    limit = 2
    response = json.loads(
        urllib.request.urlopen(url.format(page, limit)).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['videos']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)


@app.route('/search', methods=['GET', 'POST'])
def avgle_search():
    print("avgle_search")
    url = 'https://api.avgle.com/v1/search/{}/{}?limit={}'
    query = '三上悠亜'
    page = 0
    limit = 2
    response = json.loads(
        urllib.request.urlopen(url.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['videos']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)


@app.route('/search_jav', methods=['GET', 'POST'])
def avgle_search_jav():
    print("avgle_search_jav")
    url = 'https://api.avgle.com/v1/jav/{}/{}?limit={}'
    query = 'sdde-480'
    page = 0
    limit = 2
    response = json.loads(
        urllib.request.urlopen(url.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['videos']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)


@app.route('/video', methods=['GET', 'POST'])
def avgle_video():
    print("avgle_video")
    url = 'https://api.avgle.com/v1/video/{}'
    vid = '51'
    response = json.loads(urllib.request.urlopen(url.format(vid)).read().decode())
    print(response)
    if response['success']:
        categories = response['response']['video']
        return jsonutils.get_success_data(categories)
    return jsonutils.get_error_msg('Error when fetch data from avgle', jsonutils.PAGE_NOT_FOUND)
