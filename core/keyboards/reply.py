from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

MAIN_MENU_USER = InlineKeyboardBuilder()\

MAIN_MENU_USER.add(types.InlineKeyboardButton(
    text="Дальше",
    callback_data="main_menu_user")
)

MAIN_MENU_USER.adjust(1)
