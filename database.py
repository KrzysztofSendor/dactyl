import sqlite3
import datetime
import os

location = os.path.dirname(os.path.abspath(__file__))
db = location + '/dactyl.db'


def check_db():
    if os.path.isfile(db):
        return True
    else:
        return False


def create_db():
    try:
        conn = sqlite3.connect(db)
    except:
        return 'Couldn\'t create or connect to database.'
    try:
        c = conn.cursor()
        c.execute(
            '''
            CREATE TABLE links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link DATE NOT NULL,
                time_stamp DATETIME
            )
            '''
        )
        c.execute(
            '''
            CREATE TABLE contexts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                context TEXT,
                time_stamp DATETIME,
                id_link INTEGER NOT NULL
            )
            '''
        )
        conn.commit()
        conn.close()
    except:
        return 'Couldn\'t create data structure of database.'
    return '*Database created successfully*!'


def list(number):
    try:
        conn = sqlite3.connect(db)
    except:
        return 'Couldn\'t connect to database.'
    try:
        c = conn.cursor()
        c.execute(
            '''
            SELECT link, time_stamp FROM
            (SELECT * FROM links ORDER BY id DESC LIMIT ?) ORDER BY id
            ''', (str(number))
        )
        data = c.fetchall()
        conn.close()
        return data
    except:
        return 'There appears to be problem with database.'


def add_manual(url):
    try:
        conn = sqlite3.connect(db)
    except:
        return 'Couldn\'t connect to database.'
    try:
        c = conn.cursor()
        c.execute(
            '''
            INSERT INTO links (link, time_stamp) VALUES (?, ?)
            ''',
            (url, datetime.datetime.now())
        )
        conn.commit()
        conn.close()
        return 'Url added successfuly.'
    except:
        return 'There appears to be problem with database.'
