from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, CommandStart, BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..filters.Admin import IsAdmin



async def start_admin(message: types.Message):
    await message.answer("Hi,BOSS\nI'm ready to work")
    # await message.answer_photo(photo= 'https://arhivach.ng/storage/7/f8/7f867fbd0ad724b080e014d2c8999e80.png', caption='Пора топить и визуализировать')

async def start_users(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Hello,{user},I'm ready to work")


def register_start_admin(dp: Dispatcher):
    dp.register_message_handler(start_admin, CommandStart(), IsAdmin())
    dp.register_message_handler(start_users, CommandStart())

