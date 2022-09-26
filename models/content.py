from models import save_account, save_chat, save_msg


class Content:
    def __init__(self, message):
        self.forward_id = None
        self.text_id = None
        self.document_id = None
        self.audio_id = None
        self.voice_id = None
        self.animation_id = None
        self.photo_id = None
        self.poll_id = None
        self.location_id = None
        self.sticker_id = None
        self.contact_id = None
        self.message_id = message.message_id
        self.date = message.date
        self.user_id = save_account(message['from'])
        self.chat_id = save_chat(message.chat)
        self.message = message

    def forward(self):
        return self.message.forward_from

    def forward_date(self):
        return self.message.forward_date

    def document(self):
        return self.message.document

    def audio(self):
        return self.message.audio

    def voice(self):
        return self.message.voice

    def animation(self):
        return self.message.animation

    def photo(self):
        return self.message.photo

    def location(self):
        return self.message.location

    def sticker(self):
        return self.message.sticker

    def contact(self):
        return self.message.contact

    def text(self):
        return self.message.text

    def entities(self):
        return self.message.entities

    def poll(self):
        return self.message.poll

    def options(self):
        return self.message.poll.options

    def save(self):
        save_msg(self)
