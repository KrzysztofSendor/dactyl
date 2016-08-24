import sqlite3
import datetime
import os

db = 'dactyl.db'


def check_db():
    if os.path.isfile(db):
        return True
    else:
        return False


def create_db():
    if os.path.isfile(db):
        return 'Database already exists.'
    else:
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
    return 'Database created successfully!'
