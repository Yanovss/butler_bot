from db import database, insert
from sqlalchemy.orm import backref


class Stickers(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("stickers", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("stickers", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("stickers", lazy='dynamic'), uselist=False)
    width = database.Column(database.Integer)
    height = database.Column(database.Integer)
    emoji = database.Column(database.Text)
    set_name = database.Column(database.Text)
    is_animated = database.Column(database.Boolean)
    is_video = database.Column(database.Boolean)
    s_type = database.Column(database.Text)
    file_id = database.Column(database.Text)
    file_unique_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)


def save_stickers(content):
    sticker = content.sticker()
    row = Stickers(account_id=content.user_id
                   , chat_id=content.chat_id
                   , width=sticker.width
                   , height=sticker.height
                   , emoji=sticker.emoji
                   , set_name=sticker.set_name
                   , is_animated=sticker.is_animated
                   , is_video=sticker.is_video
                   , s_type=sticker.type
                   , file_id=sticker.file_id
                   , file_unique_id=sticker.file_unique_id
                   , file_size=sticker.file_size
                   , forward_id=content.forward_id
                   )
    content.sticker_id = insert(row)
