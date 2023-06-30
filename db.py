import sqlite3

connect = sqlite3.connect("users.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id TEXT PRIMARY KEY UNIQUE,
    lang TEXT,
    destination TEXT,
    citizenship TEXT,
    gender TEXT,
    budget TEXT,
    relocation_motive TEXT,
    climate TEXT,
    city_size TEXT,
    alone_family TEXT,
    new_language TEXT,
    priority TEXT,
    admin TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS countries(
    region TEXT,
    population TEXT,
    city_name TEXT,
    country TEXT,
    description TEXT,
    image TEXT, 
    cost_alone TEXT,
    cost_family TEXT
)""")

connect.commit()
