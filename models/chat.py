from db import database, insert
from datetime import datetime


class Chat(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    chat_id = database.Column(database.Integer)
    title = database.Column(database.Text)
    chat_type = database.Column(database.Text)
    created = database.Column(database.DateTime, nullable=False, default=datetime.now)


def save_chat(chat):
    title = chat.type
    if 'title' in chat:
        title = chat.title
    result = Chat.query.filter_by(chat_id=chat.id).first()
    if result is None:
        row = Chat(chat_id=chat.id, title=title, chat_type=chat.type)
        chat_id = insert(row)
    else:
        chat_id = result.id
    return chat_id
