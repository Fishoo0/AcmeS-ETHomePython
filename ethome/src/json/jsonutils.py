from flask import json, jsonify

BAD_REQUEST = 400
PAGE_NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500
SERVICE_UNAVAILABLE = 503


def get_error_msg(message, code=1000, data={}):
    if message is None:
        message = 'Unknown Error !'
    result = json.dumps({'code': code, 'message': message, 'data': data})
    return result


def get_success_msg(message, code=0, data={}):
    if message is None:
        message = 'Operate success!'
    result = json.dumps({'code': code, 'message': message, 'data': data})
    return result


def get_success_data(data):
    if data is not None:
        result = json.dumps({'code': 0, 'message': 'Success', 'data': data})
        return result
    return None
