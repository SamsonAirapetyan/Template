from wsgiref.util import request_uri

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="Локация", request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
