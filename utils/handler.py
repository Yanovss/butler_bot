from models import *
from config import current_user


def save_content(message):
    data = Content(message)
    if 'forward_from' in message:
        save_forward(data)
    if 'text' in message:
        save_text(data)
    if 'document' in message:
        save_doc(data)
    if 'audio' in message:
        save_audio(data)
    if 'voice' in message:
        save_voice(data)
    if 'animation' in message:
        save_animations(data)
    if 'photo' in message:
        save_photos(data)
    if 'poll' in message:
        save_polls(data)
    if 'location' in message:
        save_location(data)
    if 'sticker' in message:
        save_stickers(data)
    if 'contact' in message:
        save_contact(data)
    data.save()


def read(user_id):
    # results = Messages.query.filter_by(telegram_id=user_id).first()
    results = Messages.query.order_by(Messages.id.desc()).first()
    # return [next(result.text.value()) for result in results]
    return results.text
