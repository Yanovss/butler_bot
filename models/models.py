from db import database


class Messages(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    telegram_id = database.Column(database.Integer)
    text = database.Column(database.Text)
