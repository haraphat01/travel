import db
import handlers

def by_country(id, destination_search=False):
    user_data = handlers.fetch_info(id)
    country = f"'{user_data[3]}'"
    if destination_search:
        db.cursor.execute(f"Select * from countries where country = {country}")
    else:
        try:
            db.cursor.execute(f"Select * from countries where country = {country} AND cost_alone < {user_data[6] * 4}")
        except Exception as ex:
            db.cursor.execute(f"Select * from countries where country = {country}")
    country_data = db.cursor.fetchall()

    try:
        if (user_data[1] == "ru"):
            if (user_data[10] == "alone"):
                data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц</b>: {country_data[user_data[15]][6] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            else:
                data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц для семьи</b>: {country_data[user_data[15]][7] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            return data
        else:
            if (user_data[10] == "alone"):
                data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month</b>: {country_data[user_data[15]][6]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            else:
                data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month for family</b>: {country_data[user_data[15]][7]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            return data
    except Exception as ex:
        return -1

def by_user_preferences(id):
    user_data = handlers.fetch_info(id)
    cost = int(user_data[6])*4
    db.cursor.execute(f"Select * from countries where cost_alone < {cost} AND population < {user_data[9]}")
    country_data = db.cursor.fetchall()

    try:
        if (user_data[1] == "ru"):
            if (user_data[10] == "alone"):
                data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц</b>: {country_data[user_data[15]][6] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            else:
                data = f"<b>Страна</b>: {country_data[user_data[15]][3]}\n<b>Город</b>: {country_data[user_data[15]][2]}\n\n<b>Цена проживания в месяц для семьи</b>: {country_data[user_data[15]][7] * 88}₽\n<b>Описание</b>: {country_data[user_data[15]][4]}\n<b>Население</b>: {country_data[user_data[15]][1]} человек"
            return data
        else:
            if (user_data[10] == "alone"):
                data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month</b>: {country_data[user_data[15]][6]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            else:
                data = f"<b>Country</b>: {country_data[user_data[15]][3]}\n<b>City</b>: {country_data[user_data[15]][2]}\n\n<b>Cost of live per month for family</b>: {country_data[user_data[15]][7]}$\n<b>Description</b>: {country_data[user_data[15]][4]}\n<b>Population</b>: {country_data[user_data[15]][1]} people"
            return data
    except Exception as ex:
        return -1