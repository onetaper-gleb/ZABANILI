from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

MAIN_MENU_USER = InlineKeyboardBuilder()\

MAIN_MENU_USER.add(types.InlineKeyboardButton(
    text="Дальше",
    callback_data="main_menu_user")
)

MAIN_MENU_USER.adjust(1)

##############################################
FINISHED = InlineKeyboardBuilder()\

FINISHED.add(types.InlineKeyboardButton(
    text="Завершить",
    callback_data="main_menu_user")
)

FINISHED.adjust(1)
###############################################

def create_reply(answers, nums):
    KEYBOAD = InlineKeyboardBuilder()

    for i in answers:
        KEYBOAD.add(types.InlineKeyboardButton(
            text=i.strip(),
            callback_data=f'{i}_=_{nums}')
        )
        print(i)
    KEYBOAD.adjust(2)

    return KEYBOAD
