import sqlite3


def get_codes(code):
    result = S_F('code', 'Surveys')
    for i in result:
        if code in i:
            return True
    return False


def S_F(row, table):
    con = sqlite3.connect("../../Questionnaire.db")
    cur = con.cursor()
    if type(row) == str:
        result = cur.execute(f"""SELECT {row} FROM {table}""").fetchall()
    else:
        result = cur.execute(f"""SELECT {', '.join(row)} FROM {table}""").fetchall()
    con.commit()
    con.close()
    return result
