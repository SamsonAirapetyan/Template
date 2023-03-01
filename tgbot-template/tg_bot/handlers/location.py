from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from ..keabords.location_button import keyboard


async def location(message: types.Message):
    await message.answer("Для того чтобы отправить свою локацию\nнажмите кнопку ниже",
                         reply_markup=keyboard)


async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    await message.answer(f"Ваши координаты:\n\nВысота: {latitude}\n\nШирота: {longitude}", reply_markup=ReplyKeyboardRemove())

def getting_location(dp:Dispatcher):
    dp.register_message_handler(location, Command("show_location"))
    dp.register_message_handler(get_location, content_types=types.ContentType.LOCATION)
