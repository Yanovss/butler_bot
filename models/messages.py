from db import database, insert
from datetime import datetime
from sqlalchemy.orm import backref


class Messages(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    message_id = database.Column(database.Integer)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("message", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=True)
    chat = database.relationship('Chat', backref=backref("message", lazy='dynamic'), uselist=False)
    animation_id = database.Column(database.Integer, database.ForeignKey('animations.id'), nullable=True)
    animations = database.relationship('Animations', backref=backref("message", uselist=False))
    audio_id = database.Column(database.Integer, database.ForeignKey('audios.id'), nullable=True)
    audios = database.relationship('Audios', backref=backref("message", uselist=False))
    document_id = database.Column(database.Integer, database.ForeignKey('documents.id'), nullable=True)
    documents = database.relationship('Documents', backref=backref("message", uselist=False))
    location_id = database.Column(database.Integer, database.ForeignKey('locations.id'), nullable=True)
    locations = database.relationship('Locations', backref=backref("message", uselist=False))
    photo_id = database.Column(database.Integer, database.ForeignKey('photos.id'), nullable=True)
    photos = database.relationship('Photos', backref=backref("message", uselist=False))
    poll_id = database.Column(database.Integer, database.ForeignKey('polls.id'), nullable=True)
    polls = database.relationship('Polls', backref=backref("message", uselist=False))
    sticker_id = database.Column(database.Integer, database.ForeignKey('stickers.id'), nullable=True)
    stickers = database.relationship('Stickers', backref=backref("message", uselist=False))
    text_id = database.Column(database.Integer, database.ForeignKey('texts.id'), nullable=True)
    texts = database.relationship('Texts', backref=backref("message", uselist=False))
    voice_id = database.Column(database.Integer, database.ForeignKey('voices.id'), nullable=True)
    voices = database.relationship('Voices', backref=backref("message", uselist=False))
    created = database.Column(database.DateTime, nullable=False, default=datetime.now)


def save_msg(content):
    row = Messages(message_id=content.message_id
                   , account_id=content.user_id
                   , chat_id=content.chat_id
                   , animation_id=content.animation_id
                   , audio_id=content.audio_id
                   , document_id=content.document_id
                   , location_id=content.location_id
                   , photo_id=content.photo_id
                   , poll_id=content.poll_id
                   , sticker_id=content.sticker_id
                   , text_id=content.text_id
                   , voice_id=content.voice_id
                   )
    insert(row)
