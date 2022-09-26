import logging
import click
from aiogram import executor, types
from aiogram.types import ContentType
from config import dp, URL, app, bot
from utils import save_content
from requests import get, exceptions
from time import sleep
from db import database
from models import *


@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    print(message)
    save_content(message)
    response = get(URL + '/10')
    if response.status_code == 200:
        print('Success!')


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    save_content(message)
    try:
        response = get(URL + '/3')
        if response.status_code == 200:
            sleep(10)
    except exceptions.HTTPError as e:
        return False


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    print(msg)
    save_content(msg)
    # await bot.send_message(chat_id='1371733743', text='sdsdsd', reply_to_message_id=607)
    # await bot.forward_message(chat_id=msg.chat.id, from_chat_id='1371733743', message_id=627)
    #await bot.send_sticker(chat_id=msg.chat.id, sticker='CAACAgIAAxkBAAICxmMjrbkOaj9l-kkCCtkLTCmGrmL9AAL-AAMQIQIQPXGwhVibk2opBA')
    # await bot.send_document(chat_id=msg.chat.id, document='BQACAgIAAxkBAAICPGMjcvH-fYA4BhP6haqjEPstSsI0AAJwIQACoy8ZSb4j-LQwTqZ7KQQ')
    # await bot.send_voice(chat_id=msg.chat.id, voice='AwACAgIAAxkBAAICP2Mjcy7dQaHvu1AogP7yLubXPCUJAAJxIQACoy8ZSbh5IK0rUkPVKQQ')
    # await bot.send_poll(chat_id='1371733743', question="Родд", options=['dddd', 'dddd', 'dddd'], correct_option_id=1)

@app.cli.command()
@click.option('--drop', is_flag=True, help='drop database.')
@click.option('--create', is_flag=True, help='create database.')
def butler_bot(drop, create):
    """Initialize the database.
    :param create:
    :param drop:
    """
    """Initialize the database."""
    if drop:
        database.drop_all()
        click.echo('Dropped database.')
    if create:
        database.create_all()
        click.echo('Initialized database.')
    if not drop and not create:
        executor.start_polling(dp)


@app.shell_context_processor
def make_shell_context():
    return dict(db=database
                , Account=Account
                , Chat=Chat
                , Messages=Messages
                , Entities=Entities
                , Texts=Texts
                , Animations=Animations
                , Audios=Audios
                , Forward=Forward
                , Documents=Documents
                , Locations=Locations
                , Photos=Photos
                , Options=Options
                , Polls=Polls
                , Stickers=Stickers
                , Voices=Voices
                )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    butler_bot()

