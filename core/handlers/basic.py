import pygame
from aiogram import Bot
from aiogram.types import Message, CallbackQuery

from core.classes import User
from core.handlers.basic_user import start_registration, registration_step_2, registration_step_3

users = pygame.sprite.Group()


# Скрипт приветствует пользователя и добаляет его экземпляр в группу классов users
async def welcoming_message(message: Message):
    await message.delete()
    await message.answer(f'Добрый день всем, {message.from_user.full_name}.')
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
                case 'start_registration':
                    await registration_step_2_user(message)
                case 'registration_step_2':
                    await registration_step_3_user(message)


# Вызываем функцию из basic_user, отвечающую за регистрацию
async def start_registration_user(call: CallbackQuery):
    await start_registration(call, users)


# Вызываем функцию из basic_user
async def registration_step_2_user(message: Message):
    await registration_step_2(message, users)


# Вызываем функцию из basic_user
async def registration_step_3_user(message: Message):
    await registration_step_3(message, users)


async def registration_success_user(message: Message):
    pass