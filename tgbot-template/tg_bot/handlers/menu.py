from aiogram.dispatcher.filters import Command, Text
from aiogram import types, Dispatcher

from ..keabords.Menu import menu


async def show_menu(message: types.Message):
    await message.answer("Выберите действие ниже", reply_markup=menu)


async def motivation(message: types.Message):
    if message.text == "Платежи":
        await message.answer("Ожидается разработка данного действия\nСпасибо за ожидание")
    if message.text == "Отмена":
        await message.answer("Понял понял, повторять не надо")


def register_menu_handler(dp: Dispatcher):
    dp.register_message_handler(show_menu, Command("menu"))
    dp.register_message_handler(motivation, Text(equals=["Платежи","Отмена"]))
