import logging
import click
from aiogram import executor, types
from config import dp, URL, app
from extensions import save, read
from requests import get, exceptions
from time import sleep
from db import database
from models import Messages


@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    # print(message)
    response = get(URL + '/10')
    if response.status_code == 200:
        print('Success!')


@dp.message_handler()
async def echo(message: types.Message):
    save(message.from_user.id, message.text)
    try:
        response = get(URL + '/3')
        if response.status_code == 200:
            sleep(10)
    except exceptions.HTTPError as e:
        return False


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
    return dict(db=database, Messages=Messages)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    butler_bot()

