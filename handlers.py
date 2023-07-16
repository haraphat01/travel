import string
import tg_analytic

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fuzzywuzzy import process, fuzz

import asyncio
import aioschedule

import notify
import city_parser
import kb
import results
import text
import db
import visaAdvisory

countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
             'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bangladesh',
             'Barbados', 'Bahamas', 'Bahrain', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
             'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands',
             'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
             'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
             'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo-Brazzaville', 'Congo-Kinshasa', 'Cook Islands',
             'Costa Rica', 'Croatia', 'Cura?ao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
             'Dominican Republic', 'East Timor', 'Ecuador', 'El Salvador', 'Egypt', 'Equatorial Guinea', 'Eritrea',
             'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Federated States of Micronesia', 'Fiji',
             'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Lands', 'Gabon', 'Gambia',
             'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
             'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard and McDonald Islands',
             'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Isle of Man',
             'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan',
             'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
             'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
             'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
             'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
             'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
             'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea',
             'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
             'R?union', 'Romania', 'Rwanda', 'Saint Barth?lemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
             'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent', 'Samoa', 'San Marino',
             'S?o Tom? and Pr?ncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
             'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia',
             'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Sweden', 'Swaziland',
             'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga',
             'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda',
             'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
             'Vatican City', 'Vietnam', 'Venezuela', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia',
             'Zimbabwe',
             'Афганистан', 'Албания', 'Антарктика', 'Алжир', 'Американское Самоа', 'Андора', 'Ангола',
             'Антигуа и Барбуда', 'Азербайджан', 'Аргентина', 'Австралия', 'Австрия', 'Багамские Острова', 'Бахрейн',
             'Бангладеш', 'Армения', 'Барбадос', 'Бельгия', 'Бермудские Острова', 'Бутан', 'Боливия',
             'Босния и Герцеговина', 'Ботсвана', 'Остров Буве', 'Бразилия', 'Белиз',
             'Британская территория в Индийском океане', 'Соломоновы Острова', 'Британские Виргинские острова',
             'Бруней', 'Болгария', 'Мьянма', 'Бурунди', 'Белоруссия', 'Камбоджа', 'Камерун', 'Канада', 'Кабо-Верде',
             'Каймановы острова', 'Центральноафриканская Республика', 'Шри-Ланка', 'Чад', 'Чили',
             'Китайская Народная Республика', 'Остров Рождества', 'Кокосовые острова', 'Колумбия', 'Коморы', 'Майотта',
             'Республика Конго', 'Демократическая Республика Конго', 'Острова Кука', 'Коста-Рика', 'Хорватия', 'Куба',
             'Кипр', 'Чехия', 'Бенин', 'Дания', 'Доминика', 'Доминиканская Республика', 'Эквадор', 'Сальвадор',
             'Экваториальная Гвинея', 'Эфиопия', 'Эритрея', 'Эстония', 'Фарерские острова', 'Фолклендские острова',
             'Южная Георгия и Южные Сандвичевы острова', 'Фиджи', 'Финляндия', 'Аландские острова', 'Франция',
             'Французская Гвиана', 'Французская Полинезия', 'Французские Южные и Антарктические территории', 'Джибути',
             'Габон', 'Грузия', 'Гамбия', 'Палестина', 'Германия', 'Гана', 'Гибралтар', 'Кирибати', 'Греция',
             'Гренландия', 'Гренада', 'Гваделупа', 'Гуам', 'Гватемала', 'Гвинея', 'Гайана', 'Республика Гаити',
             'Остров Херд и острова Макдональд', 'Ватикан', 'Гондурас', 'Гонконг', 'Венгрия', 'Исландия', 'Индия',
             'Индонезия', 'Иран', 'Ирак', 'Ирландия', 'Италия', 'Кот-д’Ивуар', 'Ямайка', 'Япония', 'Казахстан',
             'Иордания', 'Кения', 'КНДР', 'Республика Корея', 'Кувейт', 'Киргизия', 'Лаос', 'Ливан', 'Лесото', 'Латвия',
             'Либерия', 'Ливия', 'Лихтенштейн', 'Литва', 'Люксембург', 'Макао', 'Мадагаскар', 'Малави', 'Малайзия',
             'Мальдивы', 'Мали', 'Мальта', 'Мартиника', 'Мавритания', 'Маврикий', 'Мексика', 'Монако', 'Монголия',
             'Молдавия', 'Черногория', 'Монтсеррат', 'Марокко', 'Мозамбик', 'Оман', 'Намибия', 'Науру', 'Непал',
             'Нидерланды', 'Кюрасао', 'Аруба', 'Синт-Мартен', 'Бонэйр, Синт-Эстатиус и Саба', 'Новая Каледония',
             'Вануату', 'Новая Зеландия', 'Никарагуа', 'Нигер', 'Нигерия', 'Ниуэ', 'Норфолк', 'Норвегия',
             'Северные Марианские острова', 'Внешние малые острова США', 'Микронезия', 'Маршалловы Острова', 'Палау',
             'Пакистан', 'Панама', 'Папуа — Новая Гвинея', 'Парагвай', 'Перу', 'Филиппины', 'Острова Питкэрн', 'Польша',
             'Португалия', 'Гвинея-Бисау', 'Восточный Тимор', 'Пуэрто-Рико', 'Катар', 'Реюньон', 'Румыния', 'Руанда',
             'Сен-Бартелеми', 'Острова Святой Елены, Вознесения и Тристан-да-Кунья', 'Сент-Китс и Невис', 'Ангилья',
             'Сент-Люсия', 'Сен-Мартен (Франция)', 'Сен-Пьер и Микелон', 'Сент-Винсент и Гренадины', 'Сан-Марино',
             'Сан-Томе и Принсипи', 'Саудовская Аравия', 'Сенегал', 'Сербия', 'Сейшельские Острова', 'Сьерра-Леоне',
             'Сингапур', 'Словакия', 'Словения', 'Сомали', 'Южно-Африканская Республика', 'Зимбабве', 'Испания',
             'Южный Судан', 'Судан', 'Западная Сахара', 'Суринам', 'Шпицберген и Ян-Майен', 'Свазиленд', 'Швеция',
             'Швейцария', 'Сирия', 'Таджикистан', 'Таиланд', 'Того', 'Токелау', 'Тонга', 'Тринидад и Тобаго',
             'Объединённые Арабские Эмираты', 'Тунис', 'Турция', 'Туркмения', 'Теркс и Кайкос', 'Тувалу', 'Уганда',
             'Украина', 'Республика Македония', 'Египет', 'Великобритания', 'Гернси', 'Джерси', 'Остров Мэн',
             'Танзания', 'Соединённые Штаты Америки', 'Виргинские Острова', 'Буркина-Фасо', 'Уругвай', 'Узбекистан',
             'Венесуэла', 'Уоллис и Футуна', 'Самоа', 'Йемен', 'Замбия']

DELAY_TIME = 0.1
router = Router()


def fetch_info(id):
    db.cursor.execute(f"Select * from users where id={id}")
    record = db.cursor.fetchone()
    return record


def update_bd(bd_field, updated_text, id) -> None:
    update = f"Update users set {bd_field}={updated_text} where id={id}"
    db.cursor.execute(update)
    db.connect.commit()


def update_experts_bd(bd_field, updated_text) -> None:
    update = f"Update experts set {bd_field}={updated_text}"
    db.cursor.execute(update)
    db.connect.commit()

@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    tg_analytic.statistics(msg.from_user.id, "/start")
    user_id = [msg.chat.id]
    alias = f"'@{msg.from_user.username}'"
    try:
        db.cursor.execute(f"INSERT INTO users(id, alias) VALUES(?, {alias})", user_id)
        db.connect.commit()
    except Exception as ex:
        print(ex)

    await msg.answer(text="Choose the language: ", reply_markup=kb.language_menu)


@router.callback_query(F.data == "ru")
async def language_confirmation_ru(callback: CallbackQuery):
    update_bd('by_country', 0, callback.from_user.id)
    msg_text = text.main_menu['menu_ru']
    record = fetch_info(callback.from_user.id)
    if record[14] == "admin":
        menu = kb.admin_menu_ru
    elif record[14] == "expert":
        menu = kb.menu_for_experts_ru
    else:
        menu = kb.menu_ru
    update_bd('lang', "'ru'", callback.from_user.id)

    text_to_edit = text.to_edit['ru']['language_confirmation']
    # await callback.message.edit_text(text="Choose the language: " + text_to_edit)
    # await callback.message.answer(text="Choose the language: ")
    await asyncio.sleep(DELAY_TIME)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "eng")
async def language_confirmation_eng(callback: CallbackQuery):
    update_bd('by_country', 0, callback.from_user.id)
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)
    if record[14] == "admin":
        menu = kb.admin_menu_eng
    elif record[14] == "expert":
        menu = kb.menu_for_experts_eng
    else:
        menu = kb.menu_eng
    update_bd('lang', "'eng'", callback.from_user.id)

    text_to_edit = text.to_edit['eng']['language_confirmation']
    # await callback.message.edit_text(text="Choose the language: " + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "check_appointments")
async def check(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    expert_id = f"'@{callback.from_user.username}'"
    db.cursor.execute(f"Select * from experts where expert_id={expert_id}")
    data = db.cursor.fetchall()
    msg_text = ""
    if record[1] == "ru":
        msg_text = f"<b>Добро пожаловать, {callback.from_user.first_name}</b>\n\n" \
                   f"В 10:00: {'Свободно' if data[0][4] == 'NULL' else data[0][4]}\n" \
                   f"В 11:00: {'Свободно' if data[0][5] == 'NULL' else data[0][5]}\n" \
                   f"В 12:00: {'Свободно' if data[0][6] == 'NULL' else data[0][6]}\n" \
                   f"В 13:00: {'Свободно' if data[0][7] == 'NULL' else data[0][7]}\n" \
                   f"В 14:00: {'Свободно' if data[0][8] == 'NULL' else data[0][8]}\n" \
                   f"В 15:00: {'Свободно' if data[0][9] == 'NULL' else data[0][9]}\n" \
                   f"В 16:00: {'Свободно' if data[0][10] == 'NULL' else data[0][10]}\n" \
                   f"В 17:00: {'Свободно' if data[0][11] == 'NULL' else data[0][11]}\n" \
                   f"В 18:00: {'Свободно' if data[0][12] == 'NULL' else data[0][12]}"
    else:
        msg_text = f"<b>Welcome, {callback.from_user.first_name}</b>\n\n" \
                   f"At 10am: {'Free' if data[0][4] == 'NULL' else data[0][4]}\n" \
                   f"At 11am: {'Free' if data[0][5] == 'NULL' else data[0][5]}\n" \
                   f"At 12am: {'Free' if data[0][6] == 'NULL' else data[0][6]}\n" \
                   f"At 1pm: {'Free' if data[0][7] == 'NULL' else data[0][7]}\n" \
                   f"At 2pm: {'Free' if data[0][8] == 'NULL' else data[0][8]}\n" \
                   f"At 3pm: {'Free' if data[0][9] == 'NULL' else data[0][9]}\n" \
                   f"At 4pm: {'Free' if data[0][10] == 'NULL' else data[0][10]}\n" \
                   f"At 5pm: {'Free' if data[0][11] == 'NULL' else data[0][11]}\n" \
                   f"At 6pm: {'Free' if data[0][12] == 'NULL' else data[0][12]}"

    menu = kb.exit_menu[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "admin")
async def admin(callback: CallbackQuery) -> None:
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['admin']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    menu = kb.admin_panel[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "statistics")
async def stats(callback: CallbackQuery):
    command = "статистика 1 пользователи команды"
    st = command.split(' ')
    await callback.message.answer(text=tg_analytic.analysis(st, callback.from_user.id))

class DeleteExpert(StatesGroup):
    country = State()
    alias = State()

@router.callback_query(F.data == "delete_expert")
async def deleteExpert(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    text_to_edit = text.to_edit[f'{record[1]}']['delete_expert']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    msg_text = text.admin_panel[f'{record[1]}']['delete_expert']['country']
    await state.set_state(DeleteExpert.country)
    await callback.message.answer(text=msg_text)

@router.message(DeleteExpert.country)
async def delete(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(country=msg.text.lower())
    country = f"'{msg.text.lower()}'"
    db.cursor.execute(f"SELECT * FROM experts where country={country}")
    data = db.cursor.fetchall()
    for expert in data:
        await msg.answer(text=f"<b>Name: </b>{expert[0]}\n"
                              f"<b>Type: </b>{expert[1]}\n"
                              f"<b>ID: </b>{expert[3]}")
    await state.set_state(DeleteExpert.alias)
    msg_text = text.admin_panel[f'{record[1]}']['delete_expert']['alias']
    await msg.answer(text=msg_text)

@router.message(DeleteExpert.alias)
async def delete(msg: Message, state: FSMContext) -> None:
    alias = f"'{msg.text.lower()}'"
    db.cursor.execute(f"DELETE from experts where expert_id={alias}")
    db.connect.commit()
    db.cursor.execute(
        f"Update users set user_type='user' where alias={alias}")
    db.connect.commit()
    await state.set_state(None)

    await msg.answer(text="✅Success")


@router.callback_query(F.data == "check_feedback")
async def checkFeedback(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    text_to_edit = text.to_edit[f'{record[1]}']['check_feedback']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.more_menu[f'{record[1]}']
    db.cursor.execute("SELECT * FROM users where feedback!='NULL'")
    data = db.cursor.fetchall()
    id = f"'{callback.from_user.id}'"
    for i in range(0, 5):
        try:
            await callback.message.answer(text=f"<b>{data[record[20] * 5 + i][19]}:</b>\n\n"
                                               f"{data[record[20] * 5 + i][17]}")
        except Exception as ex:
            db.cursor.execute(f"UPDATE users SET feedback_counter=-1 where id={id}")
            db.connect.commit()
            break

    msg_text = text.admin_panel[f'{record[1]}']['feedback']['more']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "more_feedback")
async def moreFeedback(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['feedback']['more']
    text_to_edit = text.to_edit[f'{record[1]}']['more_feedback']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.more_menu[f'{record[1]}']
    id = f"'{callback.from_user.id}'"
    db.cursor.execute(f"UPDATE users SET feedback_counter={record[22] + 1} where id={id}")
    db.connect.commit()
    db.cursor.execute("SELECT * FROM users where feedback!='NULL'")
    data = db.cursor.fetchall()

    info = fetch_info(callback.from_user.id)

    for i in range(0, 5):
        try:
            await callback.message.answer(text=f"<b>{data[info[22] * 5 + i][32]}:</b>\n\n"
                                               f"{data[info[22] * 5 + i][17]}")
        except Exception as ex:
            db.cursor.execute(f"UPDATE users SET feedback_counter=-1 where id={id}")
            db.connect.commit()
            break

    msg_text = text.admin_panel[f'{record[1]}']['feedback']['more']
    await callback.message.answer(text=msg_text, reply_markup=menu)

class EditDescription(StatesGroup):
    cityName = State()
    description = State()
    image = State()
    costAlone = State()
    costFamily = State()

@router.callback_query(F.data == "edit_description")
async def edit_description(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    text_to_edit = text.to_edit[f'{record[1]}']['edit_description']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    msg_text = text.admin_panel[f'{record[1]}']['edit']['city_name']
    await state.set_state(EditDescription.cityName)
    await callback.message.answer(text=msg_text)

@router.message(EditDescription.cityName)
async def start_edit(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    city = f"'{msg.text}'"
    menu = kb.edit_menu[f'{record[1]}']
    db.cursor.execute(f"Select * from countries where city_name LIKE ('%' || {city} || '%')")
    data = db.cursor.fetchone()
    await state.update_data(cityName=data[2])
    await state.update_data(country=data[3])
    await msg.answer(text=f"<b>City name: {data[2]}</b>\n"
                          f"<b>Country: {data[3]}</b>\n\n"
                          f"<b>Description: {data[4]}</b>\n"
                          f"<b>Image: {data[5]}</b>\n\n"
                          f"<b>Cost for one people: {data[6]}$</b>\n"
                          f"<b>Cost for family: {data[7]}$</b>", reply_markup=menu)

@router.callback_query(F.data == "start_edit")
async def edit(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['edit']['description']
    await state.set_state(EditDescription.description)
    await callback.message.answer(text=msg_text)

@router.message(EditDescription.description)
async def edit(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['edit']['image']
    await state.update_data(description=msg.text)
    await state.set_state(EditDescription.image)
    await msg.answer(text=msg_text)

@router.message(EditDescription.image)
async def edit(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['edit']['cost_alone']
    await state.update_data(image=msg.photo[-1].file_id)
    await state.set_state(EditDescription.costAlone)
    await msg.answer(text=msg_text)

@router.message(EditDescription.costAlone)
async def edit(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['edit']['cost_family']
    await state.update_data(costAlone=msg.text)
    await state.set_state(EditDescription.costFamily)
    await msg.answer(text=msg_text)

@router.message(EditDescription.costFamily)
async def edit(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(costFamily=msg.text)
    menu = kb.confirm_edit_menu[f'{record[1]}']
    data = await state.get_data()

    await msg.answer_photo(data['image'])
    await msg.answer(text=f"<b>City name: {data['cityName']}</b>\n"
                          f"<b>Country: {data['country']}</b>\n\n"
                          f"<b>Description: {data['description']}</b>\n"
                          f"<b>Cost for one people: {data['costAlone']}$</b>\n"
                          f"<b>Cost for family: {data['costFamily']}$</b>", reply_markup=menu)

@router.callback_query(F.data == "confirm_edit")
async def confirm_edit(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    data = await state.get_data()
    description = f"'{data['description']}'"
    city = f"'{data['cityName']}'"
    db.cursor.execute(
        f"Update countries set description=?, image=?, cost_alone=?, cost_family=? where city_name={city}",
        (description, data['image'], data['costAlone'], data['costFamily']))
    db.connect.commit()

    await callback.message.answer(text="✅Success")
    await state.set_state(None)

class AddExpert(StatesGroup):
    name = State()
    type = State()
    country = State()
    telegram = State()

@router.callback_query(F.data == "add_expert")
async def expert(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    text_to_edit = text.to_edit[f'{record[1]}']['add_new_expert']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)


    msg_text = text.admin_panel[f'{record[1]}']['add_expert']['name']
    await state.set_state(AddExpert.name)
    await callback.message.answer(text=msg_text)

@router.message(AddExpert.name)
async def expert(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(name=msg.text)

    await state.set_state(AddExpert.type)
    msg_text = text.admin_panel[f'{record[1]}']['add_expert']['type']
    await msg.answer(text=msg_text)

@router.message(AddExpert.type)
async def expert(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(type=visaAdvisory.english_short_to_full[msg.text.lower()])

    await state.set_state(AddExpert.country)
    msg_text = text.admin_panel[f'{record[1]}']['add_expert']['country']
    await msg.answer(text=msg_text)

@router.message(AddExpert.country)
async def expert(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(country=msg.text.lower())

    await state.set_state(AddExpert.telegram)
    msg_text = text.admin_panel[f'{record[1]}']['add_expert']['tg']
    await msg.answer(text=msg_text)

@router.message(AddExpert.telegram)
async def expert(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(telegram=msg.text)

    data = await state.get_data()
    db.cursor.execute(
        "INSERT INTO experts(name, type, country, expert_id) VALUES(?, ?, ?, ?)",
        (data['name'], data['type'], data['country'], data['telegram']))
    db.connect.commit()
    alias = f"'{data['telegram']}'"
    db.cursor.execute(
        f"Update users set user_type='expert' where alias={alias}")
    db.connect.commit()

    await msg.answer(text="✅Success")
    await state.set_state(None)

class AddCity(StatesGroup):
    country = State()
    city = State()
    population = State()
    image = State()
    description = State()
    costAlone = State()
    costFamily = State()

@router.message(AddCity.country)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(country=msg.text)

    await state.set_state(AddCity.city)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['city']
    await msg.answer(text=msg_text)

@router.message(AddCity.city)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(city=msg.text)

    await state.set_state(AddCity.population)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['population']
    await msg.answer(text=msg_text)

@router.message(AddCity.population)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(population=msg.text)

    await state.set_state(AddCity.image)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['image']
    await msg.answer(text=msg_text)

@router.message(AddCity.image)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(img=msg.photo[-1].file_id)

    await state.set_state(AddCity.description)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['description']
    await msg.answer(text=msg_text)

@router.message(AddCity.description)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(description=msg.text)

    await state.set_state(AddCity.costAlone)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['cost_alone']
    await msg.answer(text=msg_text)

@router.message(AddCity.costAlone)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(costAlone=msg.text)

    await state.set_state(AddCity.costFamily)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['cost_family']
    await msg.answer(text=msg_text)

@router.message(AddCity.costFamily)
async def add_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(costFamily=msg.text)
    data = await state.get_data()
    db.cursor.execute(
        "INSERT INTO countries(population, city_name, country, description, image, cost_alone, cost_family) VALUES(?, ?, ?, ?, ?, ?, ?)",
        (data['population'], data['city'], data['country'], data['description'], data['img'],
         int(data['costAlone']), int(data['costFamily']) ))
    db.connect.commit()

    city_parser.cities_eng.append(data['city'])
    await msg.answer(text="✅Success")
    await state.set_state(None)

@router.callback_query(F.data == "add_city")
async def city(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    msg_text = text.admin_panel[f'{record[1]}']['welcome']
    text_to_edit = text.to_edit[f'{record[1]}']['add_new_city']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    record = fetch_info(callback.from_user.id)
    await state.set_state(AddCity.country)
    msg_text = text.admin_panel[f'{record[1]}']['add_city']['country']
    await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "profile_search")
async def profile_search(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['profile_search']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    record = fetch_info(callback.from_user.id)

    menu = kb.confirm_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['before_questions']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "next")
async def next(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['before_questions']
    text_to_edit = text.to_edit[f'{record[1]}']['before_questions']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['gender']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "women")
async def women(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['gender']
    text_to_edit = text.to_edit[f'{record[1]}']['woman']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('gender', "'women'", callback.from_user.id)

    menu = kb.relocation_motive_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "man")
async def man(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['gender']
    text_to_edit = text.to_edit[f'{record[1]}']['man']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('gender', "'man'", callback.from_user.id)

    menu = kb.relocation_motive_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "1k")
async def less_2k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['budget']
    text_to_edit = text.to_edit[f'{record[1]}']['1k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    record = fetch_info(callback.from_user.id)
    update_bd('budget', 500, callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "1-3k")
async def from_1_to_3(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['budget']
    text_to_edit = text.to_edit[f'{record[1]}']['1-3k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('budget', 2000, callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "3k")
async def greater_3k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['budget']
    text_to_edit = text.to_edit[f'{record[1]}']['3k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('budget', 8000, callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "alone")
async def alone(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['alone_family']
    text_to_edit = text.to_edit[f'{record[1]}']['alone']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('alone_family', "'alone'", callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    menu = kb.destination_res[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "family")
async def alone(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['alone_family']
    text_to_edit = text.to_edit[f'{record[1]}']['with_family']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('alone_family', "'family'", callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    menu = kb.destination_res[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "yes")
async def btn_yes(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    text_to_edit = text.to_edit[f'{record[1]}']['btn_yes']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    await state.set_state(FindCity.country)
    msg_text = text.questions[f'{record[1]}']['citizenship']
    await callback.message.answer(text=msg_text)

class FindCity(StatesGroup):
    country = State()
    destination = State()

@router.message(FindCity.country)
async def find_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    if record[1] == "ru":
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries_ru, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)
            country = visaAdvisory.russian_to_english_profile_search[country[0].strip()].strip()
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET citizenship={ctr} where id={id}")
            db.connect.commit()
        except Exception:
            msg_text = text.try_again[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    else:
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)[0].lower().strip()
            if country in visaAdvisory.english_short_to_full.keys():
                country = visaAdvisory.english_short_to_full.get(country)
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET citizenship={ctr} where id={id}")
            db.connect.commit()
        except Exception:
            msg_text = text.try_again[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    await state.set_state(FindCity.destination)
    msg_text = text.questions[f'{record[1]}']['destination_country']
    await msg.answer(text=msg_text)

@router.message(FindCity.destination)
async def find_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    if record[1] == "ru":
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries_ru, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)
            country = visaAdvisory.russian_to_english_profile_search[country[0].strip()].strip()
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET destination={ctr} where id={id}")
            db.connect.commit()
            data = results.by_country(msg.from_user.id)
            menu = kb.city_menu[f'{record[1]}']
            if (data == -1):
                data = text.error[f'{record[1]}']
                menu = kb.main_menu[f'{record[1]}']
            await msg.answer_photo((results.getPhotoByCountry(id) if results.getPhotoByCountry(
                id) != -1 else "https://releika.ru/wp-content/uploads/2/e/3/2e32cdc84a47df0f4481a31b51f900e0.jpeg"),
                                   caption=data, reply_markup=menu)
        except Exception:
            msg_text = text.try_again_profile[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    else:
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)[0].lower().strip()
            if country in visaAdvisory.english_short_to_full.keys():
                country = visaAdvisory.english_short_to_full.get(country)
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET destination={ctr} where id={id}")
            db.connect.commit()
            data = results.by_country(msg.from_user.id)
            menu = kb.city_menu[f'{record[1]}']
            if (data == -1):
                data = text.error[f'{record[1]}']
                menu = kb.main_menu[f'{record[1]}']
            await msg.answer_photo((results.getPhotoByCountry(id) if results.getPhotoByCountry(
                id) != -1 else "https://releika.ru/wp-content/uploads/2/e/3/2e32cdc84a47df0f4481a31b51f900e0.jpeg"),
                                   caption=data, reply_markup=menu)
        except Exception:
            msg_text = text.try_again_profile[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    await state.set_state(None)


@router.callback_query(F.data == "no")
async def btn_no(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    text_to_edit = text.to_edit[f'{record[1]}']['btn_no']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.climate_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['climate']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "next_city")
async def nextCity(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('counter', record[15] + 1, callback.from_user.id)
    id = f"'{callback.from_user.id}'"
    if (record[16] == 0):
        data = results.by_country(callback.from_user.id)
        menu = kb.city_menu[f'{record[1]}']
        if (data == -1):
            data = text.error[f'{record[1]}']
            menu = kb.main_menu[f'{record[1]}']
        await callback.message.answer_photo((results.getPhotoByCountry(id) if results.getPhotoByCountry(
            id) != -1 else "https://releika.ru/wp-content/uploads/2/e/3/2e32cdc84a47df0f4481a31b51f900e0.jpeg"),
                                            caption=data, reply_markup=menu)
    else:
        data = results.by_user_preferences(callback.from_user.id)
        menu = kb.city_menu[f'{record[1]}']
        if (data == -1):
            data = text.error[f'{record[1]}']
            menu = kb.main_menu[f'{record[1]}']
        await callback.message.answer_photo((results.getPhotoByUserPreferences(id) if results.getPhotoByUserPreferences(
            id) != -1 else "https://releika.ru/wp-content/uploads/2/e/3/2e32cdc84a47df0f4481a31b51f900e0.jpeg"),
                                            caption=data, reply_markup=menu)


@router.callback_query(F.data == "business")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    text_to_edit = text.to_edit[f'{record[1]}']['business']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('relocation_motive', "'business'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "adventure")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    text_to_edit = text.to_edit[f'{record[1]}']['adventure']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('relocation_motive', "'adventure'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "career")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    text_to_edit = text.to_edit[f'{record[1]}']['career']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('relocation_motive', "'career'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "family_op")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    text_to_edit = text.to_edit[f'{record[1]}']['family']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('relocation_motive', "'family'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "other_motive")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    text_to_edit = text.to_edit[f'{record[1]}']['other']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('relocation_motive', "'other'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "equatorial")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['climate']
    text_to_edit = text.to_edit[f'{record[1]}']['equatorical']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('climate', "'equatorial'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "tropical")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['climate']
    text_to_edit = text.to_edit[f'{record[1]}']['tropical']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('climate', "'tropical'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "polar")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['climate']
    text_to_edit = text.to_edit[f'{record[1]}']['polar']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('climate', "'polar'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "yes_lang")
async def new_lang_yes(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['new_language']
    text_to_edit = text.to_edit[f'{record[1]}']['yes_lang']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('new_language', "'yes'", callback.from_user.id)

    menu = kb.priorities_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['priorities']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "no_lang")
async def new_lang_no(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['new_language']
    text_to_edit = text.to_edit[f'{record[1]}']['no_lang']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('new_language', "'no'", callback.from_user.id)

    menu = kb.priorities_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['priorities']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "health_system")
async def health_system(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['priorities']
    text_to_edit = text.to_edit[f'{record[1]}']['health_system']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('priority', "'health_system'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "education")
async def education(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['priorities']
    text_to_edit = text.to_edit[f'{record[1]}']['education']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('priority', "'education'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "nature")
async def nature(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['priorities']
    text_to_edit = text.to_edit[f'{record[1]}']['nature']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('priority', "'nature'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "city_life")
async def city_life(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['priorities']
    text_to_edit = text.to_edit[f'{record[1]}']['city_life']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('priority', "'city_life'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "infrastructure")
async def infrastructure(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['priorities']
    text_to_edit = text.to_edit[f'{record[1]}']['infrastructure']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('priority', "'infrastructure'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_150k")
async def population_150k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('counter', 0, callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['population']
    text_to_edit = text.to_edit[f'{record[1]}']['population_150k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('city_size', 150000, callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_200k")
async def population_200k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('counter', 0, callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['population']
    text_to_edit = text.to_edit[f'{record[1]}']['population_200k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('city_size', 1000000, callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_500k")
async def population_500k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('counter', 0, callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['population']
    text_to_edit = text.to_edit[f'{record[1]}']['population_500k']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    update_bd('city_size', 5000000, callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "spicy")
@router.callback_query(F.data == "normal")
@router.callback_query(F.data == "indifferent")
async def wait(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['neighbours']
    text_to_edit = text.to_edit[f'{record[1]}']['spicy_normal_cold']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    update_bd('by_country', 1, callback.from_user.id)
    data = results.by_user_preferences(callback.from_user.id)
    menu = kb.city_menu[f'{record[1]}']
    if (data == -1):
        data = text.error[f'{record[1]}']
        menu = kb.main_menu[f'{record[1]}']
    await callback.message.edit_text(text=data, reply_markup=menu)
    update_bd('counter', record[15] + 1, callback.from_user.id)


@router.callback_query(F.data == "language")
async def language_selection(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['choose_language']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    await callback.message.answer(text="Choose the language: ", reply_markup=kb.language_menu)


@router.callback_query(F.data == "destination_search")
async def destination_search(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['destination_search']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    id = f"'{callback.from_user.id}'"
    db.cursor.execute(f"UPDATE users SET counter=0 where id={id}")
    db.connect.commit()

    record = fetch_info(callback.from_user.id)

    menu = kb.destination_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['destination_search_question']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "country_search")
async def country_search(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination_search_question']
    text_to_edit = text.to_edit[f'{record[1]}']['country_search']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    record = fetch_info(callback.from_user.id)
    await state.set_state(FindSpecificCountry.country)
    msg_text = text.questions[f'{record[1]}']['destination_country']
    await callback.message.answer(text=msg_text)

class FindSpecificCountry(StatesGroup):
    country = State()

@router.message(FindSpecificCountry.country)
async def find_city(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    if record[1] == "ru":
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries_ru, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)
            country = visaAdvisory.russian_to_english_profile_search[country[0].strip()].strip()
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET destination={ctr} where id={id}")
            db.connect.commit()
            data = results.by_country_without_cost(msg.from_user.id)
            menu = kb.city_menu[f'{record[1]}']
            if (data == -1):
                data = text.error[f'{record[1]}']
                menu = kb.main_menu[f'{record[1]}']
            await msg.answer_photo(results.getPhotoByCountryWithoutCost(id), caption=data, reply_markup=menu)
        except Exception:
            msg_text = text.try_again_profile[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    else:
        try:
            country = process.extractOne(msg.text.lower(), visaAdvisory.countries, score_cutoff=65,
                                         scorer=fuzz.token_sort_ratio)[0].lower().strip()
            if country in visaAdvisory.english_short_to_full.keys():
                country = visaAdvisory.english_short_to_full.get(country)
            ctr = f"'{string.capwords(country)}'"
            id = f"'{msg.from_user.id}'"
            db.cursor.execute(f"UPDATE users SET destination={ctr} where id={id}")
            db.connect.commit()
            data = results.by_country_without_cost(msg.from_user.id)
            menu = kb.city_menu[f'{record[1]}']
            if (data == -1):
                data = text.error[f'{record[1]}']
                menu = kb.main_menu[f'{record[1]}']
            await msg.answer_photo(results.getPhotoByCountryWithoutCost(id), caption=data, reply_markup=menu)
        except Exception:
            msg_text = text.try_again_profile[f'{record[1]}']
            await msg.answer(text=msg_text)
            await btn_yes()
    await state.set_state(None)

class FindSpecificCity(StatesGroup):
    city = State()

@router.callback_query(F.data == "country_of_city_search")
async def country_of_city_search(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination_search_question']
    text_to_edit = text.to_edit[f'{record[1]}']['city_search']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    await state.set_state(FindSpecificCity.city)
    msg_text = text.questions[f'{record[1]}']['city']
    await callback.message.answer(text=msg_text)

@router.message(FindSpecificCity.city)
async def findSpecificCity(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    menu = kb.one_more_menu[f'{record[1]}']
    flag = True
    if record[1] == "ru":
        try:
            city = process.extractOne(msg.text.lower(), city_parser.cities_ru, score_cutoff=65,
                                      scorer=fuzz.token_sort_ratio)
            city = city_parser.cities_ru_to_eng[city[0].strip()].strip()
            ctr = f"'{city}'"
            db.cursor.execute(f"SELECT * FROM countries where city_name={ctr}")
            data = db.cursor.fetchall()

            await msg.answer_photo(results.getPhotoByCity(msg.from_user.id, ctr),
                                   caption=f"<b>Страна</b>: {data[0][3]}\n"
                                           f"<b>Город</b>: {data[0][2]}\n\n"
                                           f"<b>Цена проживания в месяц</b>: {data[0][6] * 88}₽\n"
                                           f"<b>Цена проживания в месяц для семьи: </b>{data[0][7] * 88}₽\n"
                                           f"<b>Описание</b>: {data[0][4][:200]}...\n"
                                           f"<b>Население</b>: {data[0][1]} человек",
                                   reply_markup=menu)
        except Exception:
            msg_text = text.try_again_city[f'{record[1]}']
            await msg.answer(text=msg_text)
            await state.set_state(FindSpecificCity.city)
            flag = False
    else:
        try:
            city = process.extractOne(msg.text.lower(), city_parser.cities_eng, score_cutoff=65,
                                      scorer=fuzz.token_sort_ratio)[0].strip()
            ctr = f"'{city}'"
            db.cursor.execute(f"SELECT * FROM countries where city_name={ctr}")
            data = db.cursor.fetchall()
            await msg.answer_photo(results.getPhotoByCity(msg.from_user.id, ctr),
                                   caption=f"<b>Country</b>: {data[0][3]}\n"
                                           f"<b>City</b>: {data[0][2]}\n\n"
                                           f"<b>Cost of live per month</b>: {data[0][6]}$\n"
                                           f"<b>Cost of live per month for family: </b>{data[0][7]}$\n"
                                           f"<b>Description</b>: {data[0][4]}\n"
                                           f"<b>Population</b>: {data[0][1]} people",
                                   reply_markup=menu)
        except Exception:
            msg_text = text.try_again_city[f'{record[1]}']
            await msg.answer(text=msg_text)
            await state.set_state(FindSpecificCity.city)
            flag = False

    if flag:
        await state.set_state(None)


@router.callback_query(F.data == "again")
async def tryAgain(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    await state.set_state(FindSpecificCity.city)
    msg_text = text.questions[f'{record[1]}']['city']
    await callback.message.answer(text=msg_text)



class VisaAdvisory(StatesGroup):
    citizenship = State()
    destination = State()
    last = State()


@router.message(VisaAdvisory.citizenship)
async def inputCitizenship(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.chat.id)
    try_again_text = text.try_again[f'{record[1]}']
    back = kb.back_menu[f'{record[1]}']
    if "'" in msg.text or '"' in msg.text:
        await state.set_state(VisaAdvisory.last)
        await msg.answer(text=try_again_text, reply_markup=back)
    else:
        update_bd("citizenship", f"'{msg.text}'", msg.chat.id)
        msg_text = text.questionsVisa[f'{record[1]}']['destination']
        await state.set_state(VisaAdvisory.destination)
        await msg.answer(text=msg_text)


@router.message(VisaAdvisory.destination)
async def inputDestination(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    try_again_text = text.try_again[f'{record[1]}']
    back = kb.back_menu[f'{record[1]}']
    if "'" in msg.text or '"' in msg.text:
        await state.set_state(VisaAdvisory.last)
        await msg.answer(text=try_again_text, reply_markup=back)
    else:
        update_bd("destination", f"'{msg.text}'", msg.chat.id)
        print(fetch_info(msg.from_user.id)[3], fetch_info(msg.from_user.id)[2])
    result = ""
    result = visaAdvisory.getVisaAdvisory(fetch_info(msg.from_user.id)[3], fetch_info(msg.from_user.id)[2], record[1])
    if result is None:
        await state.set_state(VisaAdvisory.citizenship)
        await msg.answer(text=try_again_text, reply_markup=back)
    else:
        await state.set_state(VisaAdvisory.last)
        await msg.answer(text=result, reply_markup=back)


@router.callback_query(F.data == "visa_advisory")
async def visa_advisory(callback: CallbackQuery, state: FSMContext) -> None:
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['visa_advisory']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)
    await state.set_state(VisaAdvisory.citizenship)
    record = fetch_info(callback.from_user.id)
    msg_text = text.questionsVisa[f'{record[1]}']['citizenship']
    await callback.message.answer(text=msg_text)


class feedbackState(StatesGroup):
    feedback = State()
    last = State()


@router.callback_query(F.data == "feedback")
async def feedbackCallback(callback: CallbackQuery, state: FSMContext) -> None:
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['feedback_menu']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    await state.set_state(feedbackState.feedback)
    msg_text = text.questions[f'{record[1]}']['feedback']
    await callback.message.answer(text=msg_text)

@router.message(feedbackState.feedback)
async def feedback(msg: Message, state: FSMContext) -> None:
    await state.set_state(feedbackState.last)
    update_bd("feedback", f"'{msg.text}'", msg.chat.id)
    record = fetch_info(msg.from_user.id)
    if record[1] == 'ru':
        await msg.answer(text="Спасибо за отзыв!")
    else:
        await msg.answer(text="Thanks for the feedback!")
    msg_text = text.main_menu['menu_eng']
    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[14] == "admin":
        if record[1] == 'ru':
            menu = kb.admin_menu_ru
        else:
            menu = kb.admin_menu_eng
    elif record[14] == "expert":
        if record[1] == 'ru':
            menu = kb.menu_for_experts_ru
        else:
            menu = kb.menu_for_experts_eng
    else:
        if record[1] == 'ru':
            menu = kb.menu_ru
        else:
            menu = kb.menu_eng
    await msg.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "contact_experts")
async def contact_experts(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[10] == "True":
        menu = kb.admin_menu[f'{record[1]}']
    else:
        menu = kb
    text_to_edit = text.to_edit[f'{record[1]}']['contact_experts']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_menu[f'{record[1]}']
    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "lawyer")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['lawyer']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['lawyer']
    update_bd('experts', "'lawyer'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "tax_prof")
async def tax_prof(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['tax_prof']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['tax_prof']
    update_bd('experts', "'tax professional'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "real_estate_agent")
async def real_estate_agent(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['real_estate_agent']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['real_estate_agent']
    update_bd('experts', "'real estate agent'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "relocation_buddy")
async def relocation_buddy(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['relocation_buddy']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['relocation_buddy']
    update_bd('experts', "'relocation buddy'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "immigration_adviser")
async def immigration_adviser(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['immigration_adviser']
    await callback.message.edit_text(text=msg_text + text_to_edit)
    await asyncio.sleep(DELAY_TIME)

    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['immigration_adviser']
    update_bd('experts', "'immigration adviser'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_menu[f'{record[1]}']
    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "book_appointment")
async def book_appointment(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.date_schedule[record[1]]
    msg_text = text.expert_country[f'{record[1]}']['time']

    await callback.message.answer(text=msg_text, reply_markup=menu)


class ContactExperts(StatesGroup):
    country = State()
    expertName = State()
    userEmail = State()


@router.message(ContactExperts.country)
async def countryCallback(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    data = await state.get_data()
    await state.update_data(country=msg.text)
    if record[1] == 'ru':
        try:
            country = visaAdvisory.russian_to_english[msg.text.lower()]
        except Exception:
            msg_text = text.error_book[f'{record[1]}']['error_country']
            await msg.answer(text=msg_text)
    else:
        country = msg.text.lower()
    expert_type = f"'{record[13]}'"
    db.cursor.execute(
        f"Select * from experts where country='{country}' AND {data['time']}='NULL' AND type={expert_type}"
    )
    info = db.cursor.fetchall()
    flag = True
    try:
        if len(info) == 0:
            await msg.answer(text="Sorry, no available experts😢")
            record = fetch_info(msg.from_user.id)
            menu = kb.date_schedule[record[1]]
            msg_text = text.expert_country[f'{record[1]}']['time']

            await msg.answer(text=msg_text, reply_markup=menu)
            await state.set_state(None)
            flag = False
        for expert in info:
            if record[1] == 'eng':
                await msg.answer(text=f"<b>Name: </b>{expert[0]}\n"
                                      f"<b>Country: </b> {expert[2].capitalize()}\n"
                                      f"<b>Expert type: </b>{expert[1].capitalize()}\n"
                                      f"<b>Alias: </b>{expert[3]}")
            else:
                country = visaAdvisory.english_to_russian[expert[2]]
                experts = visaAdvisory.english_to_russian[expert[1]]
                await msg.answer(text=f"<b>Имя: </b>{expert[0]}\n"
                                      f"<b>Страна: </b> {country.capitalize()}\n"
                                      f"<b>Тип эксперта: </b>{experts.capitalize()}\n"
                                      f"<b>Алиас: </b>{expert[3]}")
    except Exception as ex:
        await msg.answer(text=text.error_book[f'{record[1]}']['error_expert'])

    if flag:
        await state.set_state(ContactExperts.expertName)
        msg_text = text.expert_country[f'{record[1]}']['name']
        await msg.answer(text=msg_text)


@router.message(ContactExperts.expertName)
async def countryCallback(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(alias=msg.text)
    data = await state.get_data()
    expert_type = f"'{record[13]}'"
    if record[1] == 'ru':
        country = visaAdvisory.russian_to_english[data['country'].lower()]
    else:
        country = data['country'].lower()
    flag = True
    db.cursor.execute(
        f"Select * from experts where country='{country}' AND {data['time']}='NULL' AND type={expert_type}"
    )
    info = db.cursor.fetchall()
    experts_array = []
    for expert in info:
        experts_array.append(expert[3])
    if (data['alias'] not in experts_array):
        await state.set_state(ContactExperts.expertName)
        msg_text = text.error_book[f'{record[1]}']['error_input']
        await msg.answer(text=msg_text)
        flag = False
    if flag:
        await state.set_state(ContactExperts.userEmail)
        msg_text = text.input_user[f'{record[1]}']['email']
        await msg.answer(text=msg_text)


@router.message(ContactExperts.userEmail)
async def countryCallback(msg: Message, state: FSMContext) -> None:
    record = fetch_info(msg.from_user.id)
    await state.update_data(email=msg.text)
    data = await state.get_data()
    expert_type = f"'{record[13]}'"
    db.cursor.execute(
        f"Select * from experts where {data['time']}='NULL' AND type={expert_type}"
    )
    info = db.cursor.fetchall()
    for expert in info:
        expert_id = f"'{expert[3]}'"
    usermail = f"'{msg.text}'"
    if '@' not in usermail:
        msg_text = text.error_book[f'{record[1]}']['error_mail']
        await msg.answer(text=msg_text)
    else:
        db.cursor.execute(f"UPDATE experts SET {data['time']}={usermail} where expert_id={expert_id}")
        db.connect.commit()

        msg_text = text.expert_country[f'{record[1]}']['success']
        update_bd(data['time'], "'booked'", msg.from_user.id)
        await msg.answer(text=msg_text)
        await state.set_state(None)
        menu = kb.main_menu_buttons[f'{record[1]}']
        msg_text = text.main_menu[f'menu_{record[1]}']
        await msg.answer(text=msg_text, reply_markup=menu)
        alias = f"'{data['alias']}'"
        db.cursor.execute(f"SELECT * FROM users WHERE alias={alias}")
        id = db.cursor.fetchone()
        await notify.notification("У вас новая запись.\n\nYou have a new entry", id[0])


@router.callback_query(F.data == "ten")
async def ten(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    if record[19] == 'NULL':
        await state.update_data(time="ten")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)

@router.callback_query(F.data == "eleven")
async def eleven(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    if record[20] == 'NULL':
        await state.update_data(time="eleven")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)

@router.callback_query(F.data == "twelve")
async def twelve(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    if record[21] == 'NULL':
        await state.update_data(time="twelve")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "thirteen")
async def thirteen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[22] == 'NULL':
        await state.update_data(time="thirteen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "fourteen")
async def fourteen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[23] == 'NULL':
        await state.update_data(time="fourteen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "fifteen")
async def fifteen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[24] == 'NULL':
        await state.update_data(time="fifteen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "sixteen")
async def sixteen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[25] == 'NULL':
        await state.update_data(time="sixteen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)


@router.callback_query(F.data == "seventeen")
async def seventeen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[26] == 'NULL':
        await state.update_data(time="seventeen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)

@router.callback_query(F.data == "eighteen")
async def eighteen(callback: CallbackQuery, state: FSMContext):
    record = fetch_info(callback.from_user.id)
    if record[27] == 'NULL':
        await state.update_data(time="eighteen")
        await state.set_state(ContactExperts.country)
        msg_text = text.expert_country[f'{record[1]}']['country']
        await callback.message.answer(text=msg_text)
    else:
        msg_text = text.error_book[f'{record[1]}']['error_booking']
        await callback.message.answer(text=msg_text)

# text.greet.format(name=msg.from_user.full_name),
class feedback_profile_states(StatesGroup):
    feedback = State()
    last = State()
@router.callback_query(F.data == "feedback_profile")
async def feedback_profile(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    msg_text = text.main_menu[f'menu_{record[1]}']
    text_to_edit = text.to_edit[f'{record[1]}']['feedback_menu']
    await asyncio.sleep(DELAY_TIME)

    await state.set_state(feedback_profile_states.feedback)
    msg_text = text.questions[f'{record[1]}']['feedback_profile']
    await callback.message.answer(text=msg_text)

@router.message(feedback_profile_states.feedback)
async def feedback_profile_state(msg: Message, state: FSMContext) -> None:
    await state.set_state(feedback_profile_states.last)
    update_bd("feedback_profile", f"'{msg.text}'", msg.chat.id)
    record = fetch_info(msg.from_user.id)
    if record[1] == 'ru':
        await msg.answer(text="Спасибо за отзыв!")
    else:
        await msg.answer(text="Thanks for the feedback!")
    msg_text = text.main_menu['menu_eng']
    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[1] == 'ru':
        menu = kb.menu_ru
    else:
        menu = kb.menu_eng
    await msg.answer(text=msg_text, reply_markup=menu)

class feedback_visa_states(StatesGroup):
    feedback = State()
    last = State()
@router.callback_query(F.data == "feedback_visa")
async def feedback_visa(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    await asyncio.sleep(DELAY_TIME)
    await state.set_state(feedback_visa_states.feedback)
    msg_text = text.questions[f'{record[1]}']['feedback_visa']
    await callback.message.answer(text=msg_text)

@router.message(feedback_visa_states.feedback)
async def feedback_profile_state(msg: Message, state: FSMContext) -> None:
    await state.set_state(feedback_visa_states.last)
    update_bd("feedback_visa", f"'{msg.text}'", msg.chat.id)
    record = fetch_info(msg.from_user.id)
    if record[1] == 'ru':
        await msg.answer(text="Спасибо за отзыв!")
    else:
        await msg.answer(text="Thanks for the feedback!")
    msg_text = text.main_menu['menu_eng']
    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[1] == 'ru':
        menu = kb.menu_ru
    else:
        menu = kb.menu_eng
    await msg.answer(text=msg_text, reply_markup=menu)

class feedback_experts_states(StatesGroup):
    feedback = State()
    last = State()

@router.callback_query(F.data == "feedback_experts")
async def feedback_experts(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)
    await asyncio.sleep(DELAY_TIME)
    await state.set_state(feedback_experts_states.feedback)
    msg_text = text.questions[f'{record[1]}']['feedback_experts']
    await callback.message.answer(text=msg_text)

@router.message(feedback_experts_states.feedback)
async def feedback_experts_state(msg: Message, state: FSMContext) -> None:
    await state.set_state(feedback_experts_states.last)
    update_bd("feedback_experts", f"'{msg.text}'", msg.chat.id)
    record = fetch_info(msg.from_user.id)
    if record[1] == 'ru':
        await msg.answer(text="Спасибо за отзыв!")
    else:
        await msg.answer(text="Thanks for the feedback!")
    msg_text = text.main_menu['menu_eng']
    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.main_menu[f'menu_{record[1]}']
    if record[1] == 'ru':
        menu = kb.menu_ru
    else:
        menu = kb.menu_eng
    await msg.answer(text=msg_text, reply_markup=menu)