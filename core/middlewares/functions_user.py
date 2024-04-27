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


print(get_codes('1111'))
name_table = S_F_W('name_table_question', 'Surveys', f'code = {str(1111)}')[0][0]
print(S_F('question', name_table)[0][0])
