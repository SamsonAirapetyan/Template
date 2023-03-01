import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_bot.config import load_config
# from tg_bot.models.SQLLite import Database
from tg_bot.models.postgresql import Database

from tg_bot.handlers.start import register_start_admin
from tg_bot.handlers.error import register_error_handler
from tg_bot.handlers.menu import register_menu_handler
from tg_bot.handlers.purchase import register_choise
from tg_bot.handlers.catch_media import register_all_catch
from tg_bot.handlers.location import getting_location
from tg_bot.handlers.contact import register_all_contact
from tg_bot.handlers.pay_for_item import register_payments
from tg_bot.services.setting_commands import set_defoult_commands
from tg_bot.filters.Admin import IsAdmin

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    pass


def register_all_filters(dp):
    dp.filters_factory.bind(IsAdmin)


def register_all_handlers(dp):
    register_start_admin(dp)
    register_menu_handler(dp)
    register_choise(dp)
    getting_location(dp)
    register_all_contact(dp)
    register_all_catch(dp)
    register_payments(dp)
    register_error_handler(dp)


async def set_commands(bot: Bot):
    await set_defoult_commands(bot)


async def main():
    logging.basicConfig(
        level=logging.INFO, format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    # storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage
    # dp = Dispatcher(bot, storage=storage)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    # db = Database() #SQLlite
    db = Database()  # Postgress
    await db.create()

    try:
        await db.create_table_users()  # SQLlite
    except Exception as err:
        print(err)

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    await set_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

    # await db.delete_users()


if __name__ == '__main__':
    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error(f"Bot stopped!")
