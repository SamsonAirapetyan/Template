from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_defoult_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=
        [
            BotCommand('start', "Запуск бота, с начальными базовыми функциями"),
            BotCommand("motivation", "Получить мотивирующие изображения")
        ],
        scope=BotCommandScopeDefault()
    )
