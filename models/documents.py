from db import database, insert
from sqlalchemy.orm import backref


class Documents(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("documents", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("documents", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("documents", lazy='dynamic'), uselist=False)
    file_name = database.Column(database.Text)
    mime_type = database.Column(database.Integer)
    file_id = database.Column(database.Text)
    file_unique_id = database.Column(database.Text)
    file_size = database.Column(database.Integer)


def save_doc(content):
    document = content.document()
    result = Documents.query.filter_by(file_id=document.file_id).first()
    if result is None:
        row = Documents(account_id=content.user_id
                        , chat_id=content.chat_id
                        , file_name=document.file_name
                        , mime_type=document.mime_type
                        , file_id=document.file_id
                        , file_unique_id=document.file_unique_id
                        , file_size=document.file_size
                        , forward_id=content.forward_id
                        )
        content.document_id = insert(row)
    else:
        content.document_id = result.id

