import pygame
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from core.classes import User
from core.handlers.basic_user import main_menu, got_ID, q_1_type, q_2_type
from core.keyboards.reply import MAIN_MENU_USER

users = pygame.sprite.Group()


# Скрипт приветствует пользователя и добаляет его экземпляр в группу классов users
async def welcoming_message(message: Message):
    await message.delete()
    await message.answer(f'Добрый день, {message.from_user.full_name}.', reply_markup=MAIN_MENU_USER.as_markup())
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


# Вызываем функцию из basic_user, отвечающую за регистрацию
async def menu_user(call: CallbackQuery):
    await main_menu(call, users)


async def got_ID_user(message: Message):
    await got_ID(message, users)


async def q_1_type_user(message: Message):
    await q_1_type(message, users)


async def q_2_type_user(call: CallbackQuery):
    await q_2_type(call, users)