from aiogram.types import CallbackQuery, Message

from core.middlewares.functions_user import S_F


async def polls_see(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            sp = list(S_F(['id', 'name_table_question'], 'Surveys'))
            ans = []
            for j in sp:
                ans.append(f'{j[0]}. {j[1]}')
            g = "\n"
            i.action_list.append(['polls_see', await call.message.answer(f'''{g.join(ans)}''')])


async def poll_see(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            pass