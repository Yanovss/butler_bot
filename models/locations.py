from db import database, insert
from sqlalchemy.orm import backref


class Locations(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("locations", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("locations", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("locations", lazy='dynamic'), uselist=False)
    latitude = database.Column(database.Text)
    longitude = database.Column(database.Text)


def save_location(content):
    location = content.location()
    result = Locations.query.filter_by(latitude=location.latitude, longitude=location.longitude).first()
    if result is None:
        row = Locations(account_id=content.user_id
                        , chat_id=content.chat_id
                        , latitude=location.latitude
                        , longitude=location.longitude
                        , forward_id=content.forward_id
                        )
        content.location_id = insert(row)
    else:
        content.location_id = result.id


