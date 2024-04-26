import pygame
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from core.classes import User
from core.handlers.basic_user import main_menu
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
                    break
                case _:
                    pass


# Вызываем функцию из basic_user, отвечающую за регистрацию
async def menu_user(call: CallbackQuery):
    await main_menu(call, users)

