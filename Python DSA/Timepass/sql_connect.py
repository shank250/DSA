import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXIST users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
"""
)

conn.commit()

cursor.execute("""
               SELECT * FROM user
               """)

rows = cursor.fetchall()