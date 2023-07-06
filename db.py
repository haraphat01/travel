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
    ten TEXT DEFAULT FALSE,
    eleven TEXT DEFAULT FALSE,
    twelve TEXT DEFAULT FALSE,
    thirteen TEXT DEFAULT FALSE,
    fourteen TEXT DEFAULT FALSE,
    fifteen TEXT DEFAULT FALSE,
    sixteen TEXT DEFAULT FALSE,
    seventeen TEXT DEFAULT FALSE,
    eighteen TEXT DEFAULT FALSE
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

cursor.execute("""CREATE TABLE IF NOT EXISTS lawyer(
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

cursor.execute("""CREATE TABLE IF NOT EXISTS tax_prof(
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

cursor.execute("""CREATE TABLE IF NOT EXISTS real_estate_agent(
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

cursor.execute("""CREATE TABLE IF NOT EXISTS relocation_buddy(
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

cursor.execute("""CREATE TABLE IF NOT EXISTS immigration_adviser(
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
