import db
import handlers

def by_country(id):
    user_data = handlers.fetch_info(id)
    country = f"'{user_data[3]}'"
    db.cursor.execute(f"Select * from countries where country = {country} AND cost_alone < {user_data[6] * 4}")
    country_data = db.cursor.fetchall()

    try:
        if (user_data[1] == "ru"):
            data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц</b>: {country_data[user_data[15]][6] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            return data
        else:
            data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month</b>: {country_data[user_data[15]][6]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            return data
    except Exception as ex:
        return -1

def by_user_preferences(id):
    user_data = handlers.fetch_info(id)
    db.cursor.execute(f"Select * from countries where cost_alone < {user_data[6] * 4} AND population < {user_data[9]}")
    country_data = db.cursor.fetchall()

    try:
        if (user_data[1] == "ru"):
            data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц</b>: {country_data[user_data[15]][6] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            return data
        else:
            data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month</b>: {country_data[user_data[15]][6]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            return data
    except Exception as ex:
        return -1