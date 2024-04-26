from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

START_KEYBOARD = InlineKeyboardBuilder()\

START_KEYBOARD.add(types.InlineKeyboardButton(
    text="Дальше",
    callback_data="main_menu_user")
)

START_KEYBOARD.adjust(1)
