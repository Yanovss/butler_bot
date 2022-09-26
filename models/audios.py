from db import database, insert
from sqlalchemy.orm import backref


class Audios(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("audios", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("audios", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("audios", lazy='dynamic'), uselist=False)
    duration = database.Column(database.Integer)
    file_name = database.Column(database.Text)
    file_id = database.Column(database.Text)
    mime_type = database.Column(database.Integer)
    title = database.Column(database.Text)
    performer = database.Column(database.Text)
    file_unique_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)


def save_audio(content):
    audio = content.audio()
    result = Audios.query.filter_by(file_id=audio.file_id).first()
    if result is None:
        row = Audios(account_id=content.user_id
                     , chat_id=content.chat_id
                     , duration=audio.duration
                     , file_name=audio.file_name
                     , file_id=audio.file_id
                     , mime_type=audio.mime_type
                     , title=audio.title
                     , performer=audio.performer
                     , file_unique_id=audio.file_unique_id
                     , file_size=audio.file_size
                     , forward_id=content.forward_id
                     )
        content.audio_id = insert(row)
    else:
        content.audio_id = result.id