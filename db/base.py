import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    DB_NAME = 'mybot.db'
    DB_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        rating INTEGER,
        cause TEXT
    )""")
    db.commit()


def insert_survey(name, age, rating, cause):
    cursor.execute("""
    INSERT INTO survey(name, age, rating, cause)
        VALUES (?, ?, ?, ?)
    """, (name, age, rating, cause))
    db.commit()
