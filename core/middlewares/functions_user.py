import sqlite3


def get_codes():
    con = sqlite3.connect("../../Questionnaire.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT code FROM Surveys""").fetchall()
    print(result)
    con.commit()
    con.close()
    return result


print(get_codes())