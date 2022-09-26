from config import app
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy(app)


def insert(obj):
    database.session.add(obj)
    database.session.commit()
    return obj.id


def insert_without_commit(obj):
    database.session.add(obj)


def commit():
    database.session.commit()
