import sqlite3

connect = sqlite3.connect("users.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id TEXT PRIMARY KEY UNIQUE,
    lang TEXT,
    destination TEXT,
    citizenship TEXT,
    age TEXT,
    gender TEXT,
    budget TEXT,
    relocation_motive TEXT,
    climate TEXT,
    city_size TEXT,
    continent TEXT,
    medicine_level TEXT,
    educational_level TEXT,
    admin TEXT DEFAULT FALSE
)""")

connect.commit()