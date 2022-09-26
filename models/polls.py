from db import database, insert, commit, insert_without_commit
from sqlalchemy.orm import backref


class Polls(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    account_id = database.Column(database.Integer, database.ForeignKey('account.id'), nullable=False)
    account = database.relationship('Account', backref=backref("polls", lazy='dynamic'), uselist=False)
    chat_id = database.Column(database.Integer, database.ForeignKey('chat.id'), nullable=False)
    chat = database.relationship('Chat', backref=backref("polls", lazy='dynamic'), uselist=False)
    forward_id = database.Column(database.Integer, database.ForeignKey('forward.id'), nullable=True)
    forward = database.relationship('Forward', backref=backref("polls", lazy='dynamic'), uselist=False)
    poll_id = database.Column(database.Text)
    question = database.Column(database.Text)
    total_voter_count = database.Column(database.Integer)
    is_closed = database.Column(database.Boolean)
    is_anonymous = database.Column(database.Boolean)
    poll_type = database.Column(database.Text)
    allows_multiple_answers = database.Column(database.Boolean)
    correct_option_id = database.Column(database.Integer)
    explanation = database.Column(database.Text)


class Options(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    poll_id = database.Column(database.Integer, database.ForeignKey('polls.id'), nullable=False)
    poll = database.relationship("Polls", backref=backref("options", lazy=True))
    text = database.Column(database.Text)
    voter_count = database.Column(database.Integer)


def save_polls(content):
    polls = content.poll()
    row = Polls(
        account_id=content.user_id
        , chat_id=content.chat_id
        , poll_id=polls.id
        , question=polls.question
        , total_voter_count=polls.total_voter_count
        , is_closed=polls.is_closed
        , is_anonymous=polls.is_anonymous
        , poll_type=polls.type
        , allows_multiple_answers=polls.allows_multiple_answers
        , correct_option_id=polls.correct_option_id
        , explanation=polls.explanation
        , forward_id=content.forward_id
    )
    content.poll_id = insert(row)
    if 'options' in polls:
        save_options(content)


def save_options(content):
    options = content.options
    for o in options:
        insert_without_commit(
            Options(text=o.text
                    , voter_count=o.voter_count
                    , poll_id=content.poll_id
                    )
        )
    commit()

# todo "explanation_entities": []