from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink, hcode
import asyncio

from ..config import load_config
from ..misc.QIWI import Payment
from ..items import items
from ..keabords.pay_keabord import buy_keaboard, paid_keyboard
from ..misc.QIWI import NoPaymentFound, NotEnoughMoney


async def show_items(message: types.Message):
    await message.answer(
        text="1 <i>Выберите понравившийся вам товар</i>\n2. <i>Нажмите на кнопку купить</i>\n3. <i>После оплаты вернитесь и нажмите на кнопку</i> \"оплачено\" ")

    caption = """
    Название: {title}
    <i>Описание</i>
    {description}
    
    <u>Цена:</u> {price:.2f} <b>RUB</b>
    """

    await asyncio.sleep(5)
    for item in items:
        await message.answer_photo(
            photo=item.photo_link,
            caption=caption.format(
                title=item.title,
                description=item.description,
                price=item.price
            ),
            reply_markup=buy_keaboard(item_id=item.id)
        )


async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    item_id = call.data.split(":")[-1]
    item_id_new = int(item_id) - 1
    item = items[item_id_new]
    amount = item.price

    payment = Payment(amount=amount)
    payment.create()

    confif = load_config('.env')

    await call.message.answer(
        "\n".join(
            [
                f"К оплате {amount: .2f}₽ по номеру  телефона",
                "",
                hlink(confif.misc.wallet, url=payment.invoice),
            ]
        ),
        reply_markup=paid_keyboard
    )
    await state.set_state("qiwi")
    await state.update_data(payment=payment)


async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text("Отменено")
    await state.finish()


async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена")
        return
    except NotEnoughMoney:
        await call.message.answer("Недостаточно средств")
        return
    else:
        await call.message.answer("всё успешно оплачено")

    await call.message.delete_reply_markup()
    await state.finish()


def register_payments(dp: Dispatcher):
    dp.register_message_handler(show_items, Command("show_items"))
    dp.register_callback_query_handler(create_invoice, text_contains="buy")
    dp.register_callback_query_handler(cancel_payment, text="cancel", state="qiwi")
    dp.register_callback_query_handler(approve_payment, text="paid", state="qiwi")
