from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy", "item_name")

choise = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="Акции Тинькофф", callback_data=buy_callback.new(item_name="tink")),
        InlineKeyboardButton(text="Акции Альфа Банк", callback_data="buy:alpha")
    ],
    [
        InlineKeyboardButton(
            text="Отмена покупки",
            callback_data="cancel"
        )
    ]
])


def Inlinemodul(path: str):
    pearkeaboed = InlineKeyboardMarkup()
    PEAR_LINK = path
    pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)
    pearkeaboed.insert(pear_link)
    return pearkeaboed


# pearkeaboed = InlineKeyboardMarkup()
#
# PEAR_LINK = "https://www.tinkoff.ru/invest/"
#
# pear_link = InlineKeyboardButton(text="купи тут", url=PEAR_LINK)
# pearkeaboed.insert(pear_link)
