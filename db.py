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
    alone_family TEXT,
    new_language TEXT,
    priority TEXT,
    experts TEXT,
    admin TEXT,
    counter INTEGER DEFAULT 0,
    "10:00" DEFAULT FALSE,
    "11:00" DEFAULT FALSE,
    "12:00" DEFAULT FALSE,
    "13:00" DEFAULT FALSE,
    "14:00" DEFAULT FALSE,
    "15:00" DEFAULT FALSE,
    "16:00" DEFAULT FALSE,
    "18:00" DEFAULT FALSE
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS countries(
    region TEXT,
    population INTEGER,
    city_name TEXT,
    country TEXT,
    description TEXT,
    image TEXT, 
    cost_alone INTEGER,
    cost_family INTEGER
)""")

connect.commit()
