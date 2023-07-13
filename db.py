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
    user_type TEXT DEFAULT 'user',
    counter INTEGER DEFAULT 0,
    by_country INTEGER,
    feedback TEXT DEFAULT 'NULL',
    contact_experts_country TEXT,
    alias TEXT,
    feedback_counter INTEGER DEFAULT 0
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
    expert_id TEXT PRIMARY KEY UNIQUE,
    ten TEXT DEFAULT 'NULL',
    eleven TEXT DEFAULT 'NULL',
    twelve TEXT DEFAULT 'NULL',
    thirteen TEXT DEFAULT 'NULL',
    fourteen TEXT DEFAULT 'NULL',
    fifteen TEXT DEFAULT 'NULL',
    sixteen TEXT DEFAULT 'NULL',
    seventeen TEXT DEFAULT 'NULL',
    eighteen TEXT DEFAULT 'NULL' 
)""")



connect.commit()
