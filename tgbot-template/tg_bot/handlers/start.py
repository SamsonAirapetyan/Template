import sqlite3

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, CommandStart, BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..filters.Admin import IsAdmin
# from ..models.SQLLite import Database
from ..models.postgresql import Database
import logging


db = Database()


async def start_admin(message: types.Message):
    await message.answer("Hi,BOSS\nI'm ready  to work")
    # await message.answer_photo(photo= 'https://arhivach.ng/storage/7/f8/7f867fbd0ad724b080e014d2c8999e80.png', caption='Пора топить и визуализировать')


async def start_users(message: types.Message):
    user = message.from_user.first_name
    name = message.from_user.full_name
    await db.create()
    try:
        await db.add_user(id=message.from_user.id, name=name)
    except Exception as err:
        print(err)

    # count_users = db.count_users()[0] #SQLlite
    count_users = await db.count_users()
    # count_users = 1
    await message.answer(
        f"Здравтсвуйте,{user},Я готов к работе\nВы были занесены в базу\nВ базе уже <b>{count_users}</b> пользователей")
    logging.info(f"{message.from_user.full_name}, начал использование бота")


def register_start_admin(dp: Dispatcher):
    dp.register_message_handler(start_admin, CommandStart(), IsAdmin())
    dp.register_message_handler(start_users, CommandStart())
