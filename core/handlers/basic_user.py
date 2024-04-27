from aiogram.types import CallbackQuery, Message

from core.keyboards.reply import create_reply, FINISHED
from core.middlewares.functions_user import get_codes, S_F_W, S_F, find_q, find_q_1, db_append


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
                first_q = S_F(['question', 'type', 'answers', 'id'], name_table)[0]
                i.q = name_table
                if first_q[1] == 'write':
                    i.action_list.append(['got_ID', await message.answer(f'''{first_q[0]}''')])
                else:
                    reply = create_reply(first_q[2].split('_-_'), first_q[3])
                    i.action_list.append(['got_ID', await message.answer(f'''{first_q[0]}''', reply_markup=reply.as_markup())])
                i.answers.append([first_q[3]])
            else:
                i.action_list.append(['main_menu', await message.answer(f'''Попробуйте снова''')])
            break


async def q_1_type(message: Message, users):
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            ind = i.answers[-1][0]
            i.answers[-1].append(message.text)
            sp = find_q_1(ind, i.q)
            await message.delete()
            await i.action_list[-1][-1].delete()
            if sp:
                if sp[1] == 'write':
                    i.action_list.append(['got_ID', await message.answer(f'''{sp[0]}''')])
                else:
                    reply = create_reply(sp[2].split('_-_'), sp[3])
                    i.action_list.append(
                        ['got_ID', await message.answer(f'''{sp[0]}''', reply_markup=reply.as_markup())])
                i.answers.append([sp[3]])
            else:
                m = {}
                for j in i.answers:
                    m[j[0]] = j[1]
                name = i.username
                db_append(i.q, m, name)
                i.answers.clear()
                i.q = ''
                i.action_list.append(
                    ['FINISHED', await message.answer(f'''Вы прошли опрос.''', reply_markup=FINISHED.as_markup())])


async def q_2_type(call: CallbackQuery, users):
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            ind = i.answers[-1][0]
            i.answers[-1].append(call.data.split('_=_')[0])
            sp = find_q(ind, call.data.split('_=_')[0], i.q)
            await call.message.delete()
            if sp:
                if sp[1] == 'write':
                    i.action_list.append(['got_ID', await call.message.answer(f'''{sp[0]}''')])
                else:
                    reply = create_reply(sp[2].split('_-_'), sp[3])
                    i.action_list.append(
                        ['got_ID', await call.message.answer(f'''{sp[0]}''', reply_markup=reply.as_markup())])
                i.answers.append([sp[3]])
            else:
                m = {}
                for j in i.answers:
                    m[j[0]] = j[1]
                name = i.username
                db_append(i.q, m, name)
                i.answers.clear()
                i.q = ''
                i.action_list.append(
                    ['FINISHED', await call.message.answer(f'''Вы прошли опрос.''', reply_markup=FINISHED.as_markup())])

