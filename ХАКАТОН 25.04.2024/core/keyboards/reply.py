from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

MAIN_MENU_USER = InlineKeyboardBuilder()\

MAIN_MENU_USER.add(types.InlineKeyboardButton(
    text="Дальше",
    callback_data="start_registration")
)

MAIN_MENU_USER.adjust(1)
