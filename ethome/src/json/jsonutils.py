from flask import json, jsonify


def get_error_msg(message, code=1000):
    if message is None:
        message = 'Unknown Error !'
    result = json.dumps({'code': code, 'message': message})
    return result


def get_success_msg(message, code=0):
    if message is None:
        message = 'Operate success!'
    result = json.dumps({'code': code, 'message': message})
    return result
