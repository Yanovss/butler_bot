from db import database, insert, insert_without_commit, commit
from sqlalchemy.orm import backref


class Photos(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("photos", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("photos", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("photos", lazy='dynamic'), uselist=False)


class SizePhotos(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    photo_id = database.Column(database.Integer, database.ForeignKey('photos.id'), nullable=False)
    photos = database.relationship("Photos", backref=backref("photos", lazy=True))
    file_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)
    width = database.Column(database.Integer)
    height = database.Column(database.Integer)
    file_unique_id = database.Column(database.Text)


def save_photos(content):
    row = Photos(account_id=content.user_id
                 , chat_id=content.chat_id
                 , forward_id=content.forward_id
                 )
    content.photo_id = insert(row)


def save_size_photo(content):
    photos = content.photo()
    for p in photos:
        row = Photos(photo_id=content.photo_id
                     , account_id=content.user_id
                     , chat_id=content.chat_id
                     , file_id=p.file_id
                     , width=p.width
                     , height=p.height
                     , file_unique_id=p.file_unique_id
                     , file_size=p.file_size
                     )
        insert_without_commit(row)
    commit()
