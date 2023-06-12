import sqlite3

connect = sqlite3.connect("users.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id TEXT,
    lang TEXT,
    destination TEXT,
    citizenship TEXT
)""")

connect.commit()