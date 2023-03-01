import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text

from ..keabords.Choise import choise, buy_callback, Inlinemodul


async def show_items(message: types.Message):
    await message.answer(text="На выбор есть два банка\nЕсли вам ничего не нужно - нажмите кнопку отмена",
                         reply_markup=choise)


async def buy_tink(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logging.info(f"callbackdata = {call.data}")
    # logging.info(f"callbackdata dict = {callback_data}")
    # quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали в качестве Брокера Тинькофф", reply_markup=Inlinemodul("https://www.tinkoff.ru/invest/"))

async def buy_alpha(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Вы выбрали в качестве Брокера\nАльфа Банк", reply_markup=Inlinemodul("https://alfabank.ru/make-money/investments/"))

async def close(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.answer("Вы отменили покупку", show_alert=True)
    await call.message.edit_reply_markup()
    # await call.message.answer(text="Отмена действия")


def register_choise(dp: Dispatcher):
    dp.register_message_handler(show_items, Text(equals=["/items", "Инвестиции"]))
    dp.register_callback_query_handler(buy_tink, buy_callback.filter(item_name="tink"))
    dp.register_callback_query_handler(buy_alpha, buy_callback.filter(item_name="alpha"))
    dp.register_callback_query_handler(close, Text("cancel"))
