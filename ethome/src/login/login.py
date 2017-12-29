import sqlite3

from ethome.schema.db import get_db
from ethome.src.login.token import Token
from time import time, asctime


class Login:
    def __init__(self):
        """"""

    @staticmethod
    def find_user(user_name):
        print('find_user -> ', user_name)
        try:
            db = get_db()
            cur = db.execute('select * from User where name=?', (user_name,))
        except sqlite3.OperationalError:
            print('Can not find user')
        else:
            values = cur.fetchall()
            if len(values) == 1:
                return values[0]
        return None

    @staticmethod
    def register(user_name, user_password):
        if Login.find_user(user_name) is not None:
            return 'User name has been registered!'
        db = get_db()
        db.execute('insert into User(name,password,time) values (?,?,?)', (user_name, user_password, asctime()))
        db.commit()
        print("User ? has been inserted into db successfully", user_name)
        return None

    @staticmethod
    def login(user_name, user_password):
        item = Login.find_user(user_name)
        if item is not None:
            password = item[3]
            if password == user_password:
                token_obj = Token(item[0], user_name)
                get_db().execute('update User set token=? where name=?', (token_obj.get_token(), user_name))
                get_db().commit()
                print('User has login successfully ,and token has been refreshed')
                return None
            else:
                return 'Password is not correct!'
        else:
            return 'User has not registered yet, please register first'
        return 'Unknown error'

    @staticmethod
    def login_with_token(user_name):
        item = Login.find_user(user_name)
        if item is not None:
            token = item[4]
            if token is not None:
                token_obj = Token(None, None, token)
                if token_obj.verify_token():
                    return None
            return 'User(?) Token has expired!', user_name
        else:
            return 'User(?) has not been registered yet', user_name

    @staticmethod
    def logout(user_name):
        get_db().execute('update User set token=? where name=?', (None, user_name))
        get_db().commit()
        print('User(?) has logout successfully!')
        return None
