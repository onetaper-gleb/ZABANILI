from aiogram.types import CallbackQuery, Message


# Первый шаг регистрации - нужна фамилия
async def main_menu(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            # Добавляем сообщение в список, чтобы мы смогли его удалить
            i.action_list.append(['main_menu', await call.message.answer(f'''Введите ID опроса, который хотите пройти:''')])
            break


