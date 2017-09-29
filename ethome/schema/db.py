import sqlite3

from flask import g, current_app, app


def connect_db():
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    print('Initializing the database ...')
    db = get_db()

    with current_app.open_resource('schema/User.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    with current_app.open_resource('schema/Feeds.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    with current_app.open_resource('schema/Message.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    with current_app.open_resource('schema/Setting.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()
    print("Initialized the database.")


def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
