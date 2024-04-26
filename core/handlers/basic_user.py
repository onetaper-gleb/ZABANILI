from aiogram.types import CallbackQuery, Message


# Первый шаг регистрации - нужна фамилия
async def start_registration(call: CallbackQuery, users):
    await call.message.delete()
    id_us = call.message.chat.id
    for i in users:
        if i.id == id_us:
            # Добавляем сообщение в список, чтобы мы смогли его удалить
            i.action_list.append(['start_registration', await call.message.answer('Зарегистрируйтесь пожалуйста. Сперва введите фамилию')])
            break


# Второй шаг регистрации - Имя
async def registration_step_2(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.registered.append(message.text)
            await i.action_list[-1][-1].delete()
            i.action_list.append(['registration_step_2', await message.answer('Введите Имя')])
            break


# Третий шаг регистрации - Номер
async def registration_step_3(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.registered.append(message.text)
            await i.action_list[-1][-1].delete()
            i.action_list.append(['registration_step_3', await message.answer('Введите номер телефон')])
            break


# Регистрация окончена
async def registration_success(message: Message, users):
    await message.delete()
    id_us = message.chat.id
    for i in users:
        if i.id == id_us:
            i.registered.append(message.text)
            await i.action_list[-1][-1].delete()
            i.action_list.append([registration_success, ''])
            await message.answer('Вы успешно зарегистрировались')
            break