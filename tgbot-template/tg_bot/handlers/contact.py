from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from ..keabords.contact_button import keyboard


async def contact(message: types.Message):
    await message.answer("Для того, чтобы отправить свой контакт\nнажмите кнопку ниже", reply_markup=keyboard)


async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(f"Спасибо, {contact.full_name}, за предаставленный контакт\nВаш номер {contact.phone_number}",
                         reply_markup=ReplyKeyboardRemove())


async def cancel(message: types.Message):
    await message.answer("Отмена действия")


def register_all_contact(dp: Dispatcher):
    dp.register_message_handler(contact, Command("contact"))
    dp.register_message_handler(get_contact, content_types=types.ContentType.CONTACT)
    dp.register_message_handler(cancel, Text(equals=["Отмена"]))
