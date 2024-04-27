import datetime
import sqlite3


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


print(get_codes('1111'))
name_table = S_F_W('name_table_question', 'Surveys', f'code = {str(1111)}')[0][0]
print(S_F('question', name_table)[0][0])
