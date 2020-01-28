import sqlite3
from others import login
from others import id_user
from others import id_chat
from others import id_msg


def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner


@ensure_connection
def init_db(conn, force: bool = False):
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS user_data')
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            text        TEXT NOT NULL,
            mes_id      INTEGER NOT NULL,
            chat_id     INTEGER NOT NULL      
        )
    ''')

    conn.commit()


@ensure_connection
def add_member(conn, user_id: int, text: str, mes_id: int, chat_id: int):
    c = conn.cursor()
    c.execute('INSERT INTO user_data (user_id, text, mes_id, chat_id) VALUES (?, ?, ?, ?)',
              (user_id, text, mes_id, chat_id))
    conn.commit()
    row = c.fetchone()
    login.append(row[2])
    id_chat.append(row[4])
    id_msg.append(row[3])
    id_user.append(1)


@ensure_connection
def count_login(conn, user_id: int):
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_data WHERE user_id = ? LIMIT 1', (user_id,))
    (res,) = c.fetchone()
    return res
if __name__=='__maine__':
    init_db()
    add_member(user_id=111222, text='NURIK', mes_id=1010, chat_id=2020)
