from db import database, insert, commit
from datetime import datetime


class Account(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer)
    is_bot = database.Column(database.Boolean)
    first_name = database.Column(database.Text)
    last_name = database.Column(database.Text)
    username = database.Column(database.Text)
    language_code = database.Column(database.Text)
    vcard = database.Column(database.Text)
    phone_number = database.Column(database.Text)
    created = database.Column(database.DateTime, nullable=False, default=datetime.now)


def save_account(user):
    result = Account.query.filter_by(user_id=user.id).first()
    if result is None:
        row = Account(user_id=user.id
                      , is_bot=user.is_bot
                      , first_name=user.first_name
                      , last_name=user.last_name
                      , username=user.username
                      , language_code=user.language_code)
        user_id = insert(row)
    else:
        user_id = result.id
        if result.is_bot is None:
            result.is_bot = user.is_bot
        if result.username is None:
            result.username = user.username
        if result.language_code is None:
            result.language_code = user.language_code
        commit()
    return user_id


def save_contact(contact):
    result = Account.query.filter_by(user_id=contact.user_id).first()
    if result is None:
        row = Account(user_id=contact.user_id
                      , is_bot=0
                      , first_name=contact.first_name
                      , last_name=contact.last_name
                      , phone_number=contact.phone_number)
        insert(row)
    elif result.phone_number is None or result.phone_number != contact.phone_number:
        result.phone_number = contact.phone_number
        commit()
    if 'vcard' in contact or result.vcard is None:
        result.vcard = contact.vcard
        commit()
