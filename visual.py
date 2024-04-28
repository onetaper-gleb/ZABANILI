import sqlite3
import graphviz


def sp_for_visual(name):
    Flag = True
    ans = []
    db = sqlite3.connect(r'Questionnaire.db')
    cursor = db.cursor()
    names = cursor.execute(f"""SELECT id, type, question, required_question, required_answer FROM {name}""").fetchall()
    for i in names:
        ans.append(list(i))
    return ans


def make_new_tables():
    db = sqlite3.connect(r'../../Questionnaire.db')
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
    # print(f"Answers_{mmm}")
    # print(f"Questions_{mmm}")
    cursor.execute(
        f"""CREATE TABLE Questions_{mmm} (id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, question TEXT, answers 
        TEXT, required_question TEXT, required_answer TEXT) """)
    cursor.execute(
        f"""CREATE TABLE Answers_{mmm} (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, user_organization TEXT, 
        user_answers TEXT, poll_datetime TEXT) """)
    return mmm


def get_table_pic(dannie: list):
    sled = dannie
    # node_attr={'shape': 'rectangles'}
    dot = graphviz.Digraph()
    for s in sled:
        if s[-2]:
            dot.node(str(s[0]), s[2])
            if s[-1]:
                dot.edge(s[-2], str(s[0]), s[-1])
            else:
                dot.edge(s[-2], str(s[0]), 'Выбор')
        else:
            dot.node(str(s[0]), s[2])
    dot.render('Table', format='png')


# get_table_pic([[1, '2', ''], [2, '3', 'Да']])
