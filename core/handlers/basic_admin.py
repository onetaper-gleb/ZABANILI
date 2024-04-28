from aiogram.types import CallbackQuery, Message

from core.keyboards.reply import INFO_INLINE, STARTER, F_BACK
from core.middlewares.functions_user import S_F, S_F_W, db_append_2


async def polls_see(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            sp = list(S_F(['id', 'name'], 'Surveys'))
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
            m = S_F_W('*', 'Surveys', f"id = '{int(message.text)}'")[0]
            await i.action_list[-1][-1].delete()
            await message.answer(f'{m[0]}. {m[1]} \nПароль: {m[4]}', reply_markup=INFO_INLINE.as_markup())


async def create_name(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            i.action_list.append(['create_name', await call.message.answer('Напишите название опроса')])
            break


async def starter(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            await i.action_list[-1][-1].delete()
            if i.q == '':
                i.q = message.text
                i.poll.append([1])
            elif message.text == '+':
                i.poll.append([len(i.poll) + 1])
            else:
                code = db_append_2(i.poll, i.q)
                await message.answer(f'''Поздравляем с созданием опроса, код опроса:\n{code}''', reply_markup=F_BACK.as_markup())
                break
            i.action_list.append(['type', await message.answer('Выберите тип', reply_markup=STARTER.as_markup())])
            break


async def need_question(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            i.action_list[-1][-1].delete()
            if call.data.split('_')[1] == 'test':
                i.poll[-1].append('test')
            else:
                i.poll[-1].append('write')
            i.action_list.append(
                    ['need_question', await call.message.answer(f'Айди вопроса: {i.poll[-1][0]} \nВведите вопрос')])
            break


async def link_id(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.action_list[-1][-1].delete()
            print(i.poll)
            i.poll[-1].append(message.text)
            if i.poll[-1][1] == 'test':
                i.action_list.append(
                    ['cycle', await message.answer(f'''Выводите варианты ответа, напишите "стоп", когда 
                    введёте все варианты''')])
            else:
                i.poll[-1].append('None')
                i.action_list.append(
                    ['link_id', await message.answer(f'''Выведите ID вопроса, после которого, должен выйти этот''')])


async def cycle(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            if message.text.lower() != 'стоп':
                i.anws.append(message.text)
                i.action_list.append(['cycle', ''])
            else:
                i.poll[-1].append('_-_'.join(i.anws))
                i.anws = []
                i.action_list.append(['link_id', await message.answer(f'''Выведите ID вопроса, после которого, должен выйти этот''')])


async def link_answer(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.action_list[-1][-1].delete()
            i.poll[-1].append(message.text)
            i.action_list.append(['link_answer',
                                 await message.answer(f'''Выведите Вариант ответа, после которого, должен выйти этот 
                                 вопрос''')])
            break


async def mes_poll(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.action_list[-1][-1].delete()
            i.poll[-1].append(message.text)
            i.action_list.append(['create_name',
                                 await message.answer(f'''Напишите +, если хотите продолжить Работу над создание опроса?''')])
            break


