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
    by_country INTEGER,
    feedback TEXT,
    contact_experts_country TEXT
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

cursor.execute("""CREATE TABLE IF NOT EXISTS experts(
    name TEXT,
    type TEXT,
    country TEXT,
    user_id TEXT,
    ten TEXT,
    eleven TEXT,
    twelve TEXT,
    thirteen TEXT,
    fourteen TEXT,
    fifteen TEXT,
    sixteen TEXT,
    seventeen TEXT,
    eighteen TEXT 
)""")



connect.commit()
