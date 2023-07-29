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
    budget TEXT DEFAULT '8000',
    relocation_motive TEXT,
    climate TEXT,
    city_size TEXT DEFAULT '100000000',
    alone_family TEXT,
    new_language TEXT,
    priority TEXT,
    experts TEXT,
    user_type TEXT DEFAULT 'user',
    counter INTEGER DEFAULT 0,
    by_country INTEGER,
    feedback TEXT DEFAULT 'NULL',
    feedback_profile TEXT DEFAULT 'NULL',
    feedback_visa TEXT DEFAULT 'NULL',
    feedback_experts TEXT DEFAULT 'NULL',
    contact_experts_country TEXT,
    feedback_counter INTEGER DEFAULT 0,
    alias TEXT,
    new_users INTEGER DEFAULT 0
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
    expert_id TEXT PRIMARY KEY UNIQUE
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS booking(
    expert_type TEXT,
    email TEXT,
    country TEXT
)""")



connect.commit()
