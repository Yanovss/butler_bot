from db import database
from models import Messages


def save(user_id, text):
    prod = Messages(telegram_id=user_id, text=text)
    database.session.add(prod)
    database.session.commit()


def read(user_id):
    # results = Messages.query.filter_by(telegram_id=user_id).first()
    results = Messages.query.order_by(Messages.id.desc()).first()
    # return [next(result.text.value()) for result in results]
    return results.text
