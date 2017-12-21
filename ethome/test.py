import base64
import time
import uuid


def test():
    return uuid.uuid1('Fish', 'UserName').hex


def test_base64():
    value = base64.b64encode('What the fuck'.encode('ascii'))
    return value


def test_base64_decode():
    value = "V2hhdCB0aGUgZnVjaw=="
    print(time.time() * 1000)
    return base64.b64decode(value)
