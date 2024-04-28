import datetime
import sqlite3
from random import randint

import xlwt


def get_codes(code):
    result = S_F('code', 'Surveys')
    for i in result:
        if code in i:
            return True
    return False


def S_F(row, table):
    con = sqlite3.connect("Questionnaire.db")
    cur = con.cursor()
    if type(row) == str:
        result = cur.execute(f"""SELECT {row} FROM {table}""").fetchall()
    else:
        result = cur.execute(f"""SELECT {', '.join(row)} FROM {table}""").fetchall()
    con.commit()
    con.close()
    return result


def S_F_W(row, table, where):
    con = sqlite3.connect("Questionnaire.db")
    cur = con.cursor()
    if type(row) == str:
        result = cur.execute(f"""SELECT {row} FROM {table}
WHERE {where}""").fetchall()
    else:
        result = cur.execute(f"""SELECT {', '.join(row)} FROM {table}
WHERE {where}""").fetchall()
    con.commit()
    con.close()
    return result


def find_q(id, ans, iq):
    ans = S_F_W(['question', 'type', 'answers', 'id'], iq, f'(required_answer = "{ans}" AND required_question = "{id}")')
    if ans:
        return ans[0]
    else:
        return False


def find_q_1(id, iq):
    ans = S_F_W(['question', 'type', 'answers', 'id'], iq, f'required_question = "{id}"')
    if ans:
        return ans[0]
    else:
        return False


def db_append(iq, user_answers, user_name=''):
    con = sqlite3.connect('./Questionnaire.db')
    cur = con.cursor()
    k = cur.execute(f'''SELECT id FROM {iq}''').fetchall()
    kol_qu = len(k)
    us_an = []
    for ind in range(1, kol_qu + 1):
        if ind in user_answers:
            us_an.append(user_answers[ind])
        else:
            us_an.append('None')

    cur.execute(f'''INSERT INTO Answers_1(user_answers, user_name, poll_datetime) VALUES('{'_-_'.join(us_an)}', '{user_name}', '{datetime.datetime.now()}')''')
    con.commit()


def adminer(tg):
    for i in S_F('teg', 'Admins'):
        if tg in i:
            return True
    return False


def db_append_2(sp_que, name):
    name_table, code = make_new_tables()
    print(name_table, code)
    table_name = f'Questions_{name_table}'
    con = sqlite3.connect('Questionnaire.db')
    for i in sp_que:
        cur = con.cursor()
        count, q_type, que, answs, id_q, req_an = i

        cur.execute(
            f'''INSERT INTO {table_name}(id, type, question, answers, required_question, required_answer) VALUES('{count}', '{q_type}', '{que}', '{answs}', '{id_q}', '{req_an}')''')
        con.commit()
    cur = con.cursor()
    cur.execute(
        f"""INSERT INTO Surveys(id, name, name_table_question, name_table_answer, code) VALUES ('{name_table}', '{name}', 'Questions_{name_table}', 'Answers_{name_table}', '{code}')"""
    )
    con.commit()
    con.close()
    return code


def make_new_tables():
    db = sqlite3.connect('Questionnaire.db')
    cursor = db.cursor()
    names = """SELECT name FROM sqlite_master  
      WHERE type='table';"""
    cursor.execute(names)
    em = cursor.fetchall()
    mmm = 0
    for x in em:
        if '_' in x[0] and x[0][x[0].find('_') + 1].isdigit():
            mmm = max(mmm, int(x[0][x[0].find('_') + 1:]))
    mmm += 1
    print(f"Answers_{mmm}")
    print(f"Questions_{mmm}")
    cursor.execute(
        f"""CREATE TABLE Questions_{mmm} (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, question TEXT, answers TEXT, required_question TEXT, required_answer TEXT) """)
    cursor.execute(
        f"""CREATE TABLE Answers_{mmm} (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, user_organization TEXT, user_answers TEXT, poll_datetime TEXT) """)
    code = randint(1000, 10000)
    return mmm, code


def export_to_xls(ans_table_name, qu_table_name):
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Python Sheet 1")

    con = sqlite3.connect('./Questionnaire.db')
    cur = con.cursor()
    table_ans = cur.execute(f'''SELECT * FROM {ans_table_name}''').fetchall()
    questions = cur.execute(f'''SELECT question FROM {qu_table_name}''').fetchall()

    #  Верхний колонтикул
    sheet1.write(0, 0, "Имя пользователя")
    sheet1.write(0, 1, "Организация")
    for i in range(len(questions)):
        sheet1.write(0, i + 2, questions[i])
    sheet1.write(0, i + 3, "Дата и время прохождения")

    #  Основное содержимое
    for el in table_ans:
        id, us_name, org, us_ans, date = el
        user_answers_list = us_ans.split('_-_')
        sheet1.write(id, 0, us_name)
        sheet1.write(id, 1, org)
        for k in range(len(user_answers_list)):
            if user_answers_list[k] != 'None':
                sheet1.write(id, k + 2, user_answers_list[k])
        sheet1.write(id, k + 3, date)

    book.save("User_answers.xls")


def exel(bd, count):
    sp = []
    sp2 = []
    sp3 = []

    conn = sqlite3.connect(bd)
    cursor = conn.cursor()

    cursor.execute("""select * from sqlite_master where type = 'table'""")
    tables = cursor.fetchall()

    for table in tables:
        sp.append(table[1])

    for el in sp:
        if len(el.split("_")) > 1:
            sp2.append(el.split("_"))
    for el in sp2:
        if str(el[-1]) == str(count):
            sp3.append(f"{el[0]}_{el[-1]}")
    return sp3