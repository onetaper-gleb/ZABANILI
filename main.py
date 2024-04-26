import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from magic_filter import F

from core.handlers.basic import welcoming_message, menu_user
from core.settings import settings
from core.utills.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, 'Bot has just started working')


async def end_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Bot finished it's work")


async def start():
    bot = Bot(token=settings.bots.bot_token)
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)
    dp.message.register(welcoming_message, Command(commands=['start']))
    dp.callback_query.register(menu_user, F.data == 'main_menu_user')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
