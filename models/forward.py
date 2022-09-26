from db import database, insert
from sqlalchemy.orm import backref


class Forward(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("forward", lazy='dynamic'), uselist=False)
    created = database.Column(database.DateTime, nullable=False)


def save_forward(content):
    result = Forward.query.filter_by(account_id=content.user_id, created=content.forward_date()).first()
    if result is None:
        row = Forward(account_id=content.user_id, created=content.forward_date)
        content.forward_id = insert(row)
    else:
        content.forward_id = result.id






