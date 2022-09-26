from db import database, insert, commit, insert_without_commit
from sqlalchemy.orm import backref


class Texts(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    text = database.Column(database.Text)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("texts", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("texts", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("texts", lazy='dynamic'), uselist=False)


class Entities(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    text_id = database.Column(database.Integer, database.ForeignKey('texts.id'), nullable=False)
    text = database.relationship("Texts", backref=backref("entities", lazy=True))
    e_type = database.Column(database.Text)
    e_offset = database.Column(database.Integer)
    e_length = database.Column(database.Integer)


def save_text(content):
    text = content.text()
    result = Texts.query.filter_by(text=text).first()
    if result is None:
        row = Texts(text=text
                    , account_id=content.user_id
                    , chat_id=content.chat_id
                    , forward_id=content.forward_id
                    )
        content.text_id = insert(row)
        if 'entities' in content.message:
            save_entities(content)
    else:
        content.text_id = result.id


def save_entities(content):
    for e in content.entities:
        insert_without_commit(
            Entities(text_id=content.text_id,
                     e_type=e.type,
                     e_offset=e.offset,
                     e_length=e.length
                     )
        )
    commit()

