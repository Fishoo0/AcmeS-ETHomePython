import os,json

from flask import Flask

from ethome.schema.db import init_db, close_db
from ethome.src.login.token import Token

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
    return "Welcome to ET Home Website !"


@app.route('/token_encode')
def test_token_encode():
    token = Token("1234", "fish", None)
    return token.get_token()


@app.route('/token_decode')
def test_token_decode():
    token = Token(None, None, 'MTIzNDpmaXNoOjE1MTQyNTQ1NzYuOTAzNzY0')
    return str(token.verify_token())

@app.route('/hello')
def hello_python():
    return "FUCK"

