import pygame
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from core.classes import User
from core.handlers.basic_admin import polls_see, poll_see, create_name, starter, need_question, link_id, cycle, \
    link_answer, mes_poll, view_call, exel_call
from core.handlers.basic_user import main_menu, got_ID, q_1_type, q_2_type
from core.keyboards.reply import MAIN_MENU_USER, MAIN_MENU_ADMIN
from core.middlewares.functions_user import adminer

users = pygame.sprite.Group()


# Скрипт приветствует пользователя и добаляет его экземпляр в группу классов users
async def welcoming_message(message: Message):
    await message.delete()
    if not adminer(f'@{message.from_user.username}'):
        await message.answer(f'Добрый день, {message.from_user.full_name}.', reply_markup=MAIN_MENU_USER.as_markup())
    else:
        await message.answer(f'Добрый день, {message.from_user.full_name}.', reply_markup=MAIN_MENU_ADMIN.as_markup())
    id_us = message.chat.id
    name = message.from_user.username
    # Цикл регистрации события для определённого пользователя
    for i in users:
        if i.id == id_us:
            break
    else:
        User(message.from_user.id, name, id_us, users, welcoming_message)


async def reg_messsage(message: Message, bot: Bot):
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            match i.action_list[-1][0]:
                case 'main_menu':
                    await got_ID_user(message)
                case 'got_ID':
                    await q_1_type_user(message)
                case 'polls_see':
                    await poll_see_admin(message)
                case 'create_name':
                    await starter_admin(message)
                case 'need_question':
                    await link_id_admin(message)
                case 'cycle':
                    await cycle_admin(message)
                case 'link_id':
                    await link_answer_admin(message)
                case 'link_answer':
                    await mes_poll_admin(message)


# Вызываем функцию из basic_user, отвечающую за регистрацию
async def menu_user(call: CallbackQuery):
    await main_menu(call, users)


async def got_ID_user(message: Message):
    await got_ID(message, users)


async def q_1_type_user(message: Message):
    await q_1_type(message, users)


async def q_2_type_user(call: CallbackQuery):
    await q_2_type(call, users)


async def polls_see_admin(call: CallbackQuery):
    await polls_see(call, users)


async def poll_see_admin(message: Message):
    await poll_see(message, users)


async def create_name_admin(call: CallbackQuery):
    await create_name(call, users)


async def starter_admin(message: Message):
    await starter(message, users)


async def need_question_admin(call: CallbackQuery):
    await need_question(call, users)


async def link_id_admin(message: Message):
    await link_id(message, users)


async def cycle_admin(message: Message):
    await cycle(message, users)


async def link_answer_admin(message: Message):
    await link_answer(message, users)


async def mes_poll_admin(message: Message):
    await mes_poll(message, users)


async def view_call_admin(call: CallbackQuery):
    await view_call(call, users)


async def exel_call_admin(call: CallbackQuery):
    await exel_call(call, users)