from aiogram.types import CallbackQuery, Message

from core.middlewares.functions_user import get_codes, S_F_W, S_F


# Первый шаг регистрации - нужна фамилия
async def main_menu(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            # Добавляем сообщение в список, чтобы мы смогли его удалить
            i.action_list.append(['main_menu', await call.message.answer(f'''Введите ID опроса, который хотите пройти:''')])
            break


async def got_ID(message: Message, users):
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            await message.delete()
            await i.action_list[-1][-1].delete()
            if get_codes(message.text):
                name_table = S_F_W('name_table_question', 'Surveys', f'code = {str(1111)}')[0][0]
                first_q = S_F('question', name_table)[0][0]
                i.action_list.append(['got_ID', await message.answer(f'''{first_q}''')])
            else:
                i.action_list.append(['main_menu', await message.answer(f'''Попробуйте снова''')])
            break