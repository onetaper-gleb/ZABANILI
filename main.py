import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F

from core.handlers.basic import welcoming_message, menu_user, reg_messsage, q_2_type_user, polls_see_admin, \
    create_name_admin, need_question_admin, view_call_admin, exel_call_admin
from core.handlers.basic_admin import need_question, view_call
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
    dp.callback_query.register(polls_see_admin, F.data == 'View_polls')
    dp.callback_query.register(create_name_admin, F.data == 'Create_poll')
    dp.callback_query.register(view_call_admin, F.data == 'view_call')
    dp.callback_query.register(exel_call_admin, F.data == 'exel_call')
    dp.callback_query.register(need_question_admin, F.data.startswith('que'))
    dp.message.register(reg_messsage, F.text)
    dp.callback_query.register(q_2_type_user)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
