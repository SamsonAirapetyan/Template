from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

admin = [705820014]


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user_id = message.from_user.id
        return user_id in admin
