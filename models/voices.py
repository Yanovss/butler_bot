from db import database, insert
from sqlalchemy.orm import backref
from config import current_user


class Voices(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("voices", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("voices", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("voices", lazy='dynamic'), uselist=False)
    duration = database.Column(database.Integer)
    mime_type = database.Column(database.Integer)
    file_unique_id = database.Column(database.Text)
    file_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)


def save_voice(content):
    voice = content.voice()
    row = Voices(account_id=content.user_id
                 , chat_id=content.chat_id
                 , duration=voice.duration
                 , file_name=voice.file_name
                 , file_id=voice.file_id
                 , mime_type=voice.mime_type
                 , file_unique_id=voice.file_unique_id
                 , file_size=voice.file_size
                 , forward_id=content.forward_id
                 )
    content.voice_id = insert(row)