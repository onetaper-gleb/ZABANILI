from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

################################################

MAIN_MENU_ADMIN = InlineKeyboardBuilder()\

MAIN_MENU_ADMIN.add(types.InlineKeyboardButton(
    text="Посмотреть Опросы",
    callback_data="View_polls")
)

MAIN_MENU_ADMIN.add(types.InlineKeyboardButton(
    text="Создать Опрос",
    callback_data="Create_poll")
)


MAIN_MENU_ADMIN.adjust(2)

###########################################

INFO_INLINE = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Изменить",
            callback_data="change_call"
        )
    ],
    [
        InlineKeyboardButton(
            text="Закрыть опрос",
            callback_data="close_call"
        )
    ],
    [
        InlineKeyboardButton(
            text="Просмотреть карту",
            callback_data="view_call"
        )
    ],
    [
        InlineKeyboardButton(
            text="Показ в Exel",
            callback_data="exel_call"
        )
    ]
])