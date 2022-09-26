from db import database, insert
from sqlalchemy.orm import backref


class Animations(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("animations", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("animations", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("animations", lazy='dynamic'), uselist=False)
    file_name = database.Column(database.Text)
    mime_type = database.Column(database.Integer)
    duration = database.Column(database.Integer)
    file_id = database.Column(database.Text)
    file_unique_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)
    width = database.Column(database.Integer)
    height = database.Column(database.Integer)


def save_animations(content):
    animations = content.animation()
    result = Animations.query.filter_by(file_id=animations.file_id).first()
    if result is None:
        row = Animations(account_id=content.user_id
                         , chat_id=content.chat_id
                         , duration=animations.duration
                         , file_name=animations.file_name
                         , file_id=animations.file_id
                         , mime_type=animations.mime_type
                         , width=animations.width
                         , height=animations.height
                         , file_unique_id=animations.file_unique_id
                         , file_size=animations.file_size
                         , forward_id=content.forward_id
                         )
        content.animation_id = insert(row)
    else:
        content.animation_id = result.id
