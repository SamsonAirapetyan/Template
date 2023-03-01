import logging

from aiogram import Dispatcher
from aiogram.types import Update


async def errors_handler(update, exception):
    from aiogram.utils.exceptions import (Unauthorized, InvalidUserId, TelegramAPIError, CantDemoteChatCreator,
                                          InvalidQueryID, CantParseEntities)

    if isinstance(exception, CantDemoteChatCreator):
        logging.info("Cant demote chat creator")
        return True
    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer("Попал в error хендлер")
        return True

    if isinstance(exception, InvalidUserId):
        logging.info("Invalid User ID")
        return True
    if isinstance(exception, InvalidQueryID):
        logging.info("Invalid Query ID")
        return True

    logging.exception(f"Update: {update} \n {exception}")


def register_error_handler(dp: Dispatcher):
    dp.register_message_handler(errors_handler)
