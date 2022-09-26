import os
from flask import Flask
from aiogram.dispatcher import Dispatcher
from aiogram import Bot

prefix = 'sqlite:///'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'bot_data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

TOKEN = os.getenv('BOT_TOKEN')
URL = os.getenv('URL')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


current_user = {'user_id': 0, 'chat_id': 0, 'msg_id': 0, 'forward_id': None}
