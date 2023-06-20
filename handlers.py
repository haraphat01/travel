from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import asyncio
import aioschedule

import kb
import text
import db
import visaAdvisory

countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bangladesh', 'Barbados', 'Bahamas', 'Bahrain', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo-Brazzaville', 'Congo-Kinshasa', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cura?ao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'El Salvador', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Lands', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard and McDonald Islands', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Isle of Man', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'R?union', 'Romania', 'Rwanda', 'Saint Barth?lemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent', 'Samoa', 'San Marino', 'S?o Tom? and Pr?ncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Sweden', 'Swaziland', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Vietnam', 'Venezuela', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe',
             'Афганистан','Албания','Антарктика','Алжир','Американское Самоа','Андора','Ангола','Антигуа и Барбуда','Азербайджан','Аргентина','Австралия','Австрия','Багамские Острова','Бахрейн','Бангладеш','Армения','Барбадос','Бельгия','Бермудские Острова','Бутан','Боливия','Босния и Герцеговина','Ботсвана','Остров Буве','Бразилия','Белиз','Британская территория в Индийском океане','Соломоновы Острова','Британские Виргинские острова','Бруней','Болгария','Мьянма','Бурунди','Белоруссия','Камбоджа','Камерун','Канада','Кабо-Верде','Каймановы острова','Центральноафриканская Республика','Шри-Ланка','Чад','Чили','Китайская Народная Республика','Остров Рождества','Кокосовые острова','Колумбия','Коморы','Майотта','Республика Конго','Демократическая Республика Конго','Острова Кука','Коста-Рика','Хорватия','Куба','Кипр','Чехия','Бенин','Дания','Доминика','Доминиканская Республика','Эквадор','Сальвадор','Экваториальная Гвинея','Эфиопия','Эритрея','Эстония','Фарерские острова','Фолклендские острова','Южная Георгия и Южные Сандвичевы острова','Фиджи','Финляндия','Аландские острова','Франция','Французская Гвиана','Французская Полинезия','Французские Южные и Антарктические территории','Джибути','Габон','Грузия','Гамбия','Палестина','Германия','Гана','Гибралтар','Кирибати','Греция','Гренландия','Гренада','Гваделупа','Гуам','Гватемала','Гвинея','Гайана','Республика Гаити','Остров Херд и острова Макдональд','Ватикан','Гондурас','Гонконг','Венгрия','Исландия','Индия','Индонезия','Иран','Ирак','Ирландия','Италия','Кот-д’Ивуар','Ямайка','Япония','Казахстан','Иордания','Кения','КНДР','Республика Корея','Кувейт','Киргизия','Лаос','Ливан','Лесото','Латвия','Либерия','Ливия','Лихтенштейн','Литва','Люксембург','Макао','Мадагаскар','Малави','Малайзия','Мальдивы','Мали','Мальта','Мартиника','Мавритания','Маврикий','Мексика','Монако','Монголия','Молдавия','Черногория','Монтсеррат','Марокко','Мозамбик','Оман','Намибия','Науру','Непал','Нидерланды','Кюрасао','Аруба','Синт-Мартен','Бонэйр, Синт-Эстатиус и Саба','Новая Каледония','Вануату','Новая Зеландия','Никарагуа','Нигер','Нигерия','Ниуэ','Норфолк','Норвегия','Северные Марианские острова','Внешние малые острова США','Микронезия','Маршалловы Острова','Палау','Пакистан','Панама','Папуа — Новая Гвинея','Парагвай','Перу','Филиппины','Острова Питкэрн','Польша','Португалия','Гвинея-Бисау','Восточный Тимор','Пуэрто-Рико','Катар','Реюньон','Румыния','Руанда','Сен-Бартелеми','Острова Святой Елены, Вознесения и Тристан-да-Кунья','Сент-Китс и Невис','Ангилья','Сент-Люсия','Сен-Мартен (Франция)','Сен-Пьер и Микелон','Сент-Винсент и Гренадины','Сан-Марино','Сан-Томе и Принсипи','Саудовская Аравия','Сенегал','Сербия','Сейшельские Острова','Сьерра-Леоне','Сингапур','Словакия','Словения','Сомали','Южно-Африканская Республика','Зимбабве','Испания','Южный Судан','Судан','Западная Сахара','Суринам','Шпицберген и Ян-Майен','Свазиленд','Швеция','Швейцария','Сирия','Таджикистан','Таиланд','Того','Токелау','Тонга','Тринидад и Тобаго','Объединённые Арабские Эмираты','Тунис','Турция','Туркмения','Теркс и Кайкос','Тувалу','Уганда','Украина','Республика Македония','Египет','Великобритания','Гернси','Джерси','Остров Мэн','Танзания','Соединённые Штаты Америки','Виргинские Острова','Буркина-Фасо','Уругвай','Узбекистан','Венесуэла','Уоллис и Футуна','Самоа','Йемен','Замбия']

router = Router()

def fetch_info(id):
    db.cursor.execute(f"Select * from users where id={id}")
    record = db.cursor.fetchone()
    return record

def update_bd(bd_field, updated_text, id) -> None:
    update = f"Update users set {bd_field}={updated_text} where id={id}"
    db.cursor.execute(update)
    db.connect.commit()


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    user_id = [msg.chat.id]
    try:
        db.cursor.execute("INSERT INTO users(id) VALUES(?)", user_id)
        db.connect.commit()
    except Exception as ex:
        print(ex)

    await msg.answer(text="Choose the language: ", reply_markup=kb.language_menu)

@router.callback_query(F.data == "ru")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.main_menu['menu_ru']
    record = fetch_info(callback.from_user.id)
    if record[10] == "True":
        menu = kb.admin_menu_ru
    else:
        menu = kb.menuRu
    update_bd('lang', "'ru'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "eng")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    record = fetch_info(callback.from_user.id)
    if record[10] == "True":
        menu = kb.admin_menu_eng
    else:
        menu = kb.menuEng
    update_bd('lang', "'eng'", callback.from_user.id)

    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "profile_search")
async def profile_search(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    menu = kb.confirm_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['before_questions']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "next")
async def next(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)

    menu = kb.gender_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['gender']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "women")
async def women(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('gender', "'women'", callback.from_user.id)

    menu = kb.relocation_motive_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "man")
async def man(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('gender', "'man'", callback.from_user.id)

    menu = kb.relocation_motive_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['relocation_motive']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "1k")
async def less_2k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('budget', "'500-1K'", callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "1-3k")
async def from_1_to_3(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('budget', "'1-3K'", callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "3k")
async def greater_3k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('budget', "'3-12K'", callback.from_user.id)

    menu = kb.alone_or_family[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['alone_family']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "alone")
async def alone(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('alone_family', "'alone'", callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    menu = kb.destination_res[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "family")
async def alone(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('alone_family', "'family'", callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['destination']
    menu = kb.destination_res[f'{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "yes")
async def btn_yes(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    menu = kb.citizenship_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['citizenship']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "no")
async def btn_no(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    menu = kb.climate_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['climate']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "usa")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Usa'", callback.from_user.id)


@router.callback_query(F.data == "russia")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Russia'", callback.from_user.id)


@router.callback_query(F.data == "israel")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Israel'", callback.from_user.id)


@router.callback_query(F.data == "eu")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Europe'", callback.from_user.id)


@router.callback_query(F.data == "ukraine")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Ukraine'", callback.from_user.id)


@router.callback_query(F.data == "kazah")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Kazakhstan'", callback.from_user.id)


@router.callback_query(F.data == "armenia")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Armenia'", callback.from_user.id)


@router.callback_query(F.data == "georgia")
async def usa(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('citizenship', f"'Georgia'", callback.from_user.id)


@router.callback_query(F.data == "other_country")
async def input_country(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['input_country']
    await callback.message.answer(text=msg_text)
    # await country(callback.from_user.id)

# @router.message(F.text.in_(countries))
# async def country(msg: Message):
#     record = fetch_info(msg.chat.id)
#     update_bd('citizenship', f"'{msg.text}'", msg.chat.id)
#
#     menu = kb.relocation_motive_menu[f'{record[1]}']
#     msg_text = text.questions[f'{record[1]}']['relocation_motive']
#     await msg.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "business")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('relocation_motive', "'business'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "adventure")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('relocation_motive', "'adventure'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "career")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('relocation_motive', "'career'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "family_op")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('relocation_motive', "'family'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "other_motive")
async def relocation_motive(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('relocation_motive', "'other'", callback.from_user.id)

    menu = kb.budget_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['budget']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "equatorial")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('climate', "'equatorial'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "tropical")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('climate', "'tropical'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "polar")
async def cold(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('climate', "'polar'", callback.from_user.id)

    menu = kb.lang_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['new_language']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "yes_lang")
async def new_lang_yes(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('new_language', "'yes'", callback.from_user.id)

    menu = kb.priorities_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['priorities']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "no_lang")
async def new_lang_no(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('new_language', "'no'", callback.from_user.id)

    menu = kb.priorities_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['priorities']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "health_system")
async def health_system(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('priority', "'health_system'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "education")
async def education(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('priority', "'education'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "nature")
async def nature(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('priority', "'nature'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "city_life")
async def city_life(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('priority', "'city_life'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "infrastructure")
async def infrastructure(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('priority', "'infrastructure'", callback.from_user.id)

    menu = kb.population_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['population']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_150k")
async def population_150k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('city_size', "'150k'", callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_200k")
async def population_200k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('city_size', "'200k'", callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "population_500k")
async def population_500k(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)
    update_bd('city_size', "'500k'", callback.from_user.id)

    menu = kb.neighbours_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['neighbours']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "spicy")
@router.callback_query(F.data == "normal")
@router.callback_query(F.data == "cold")
async def wait(callback: CallbackQuery) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['wait']
    await callback.message.answer(text=msg_text)

@router.callback_query(F.data == "language")
async def language_selection(callback: CallbackQuery):
    await callback.message.answer(text="Choose the language: ", reply_markup=kb.language_menu)


@router.callback_query(F.data == "destination_search")
async def destination_search(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    menu = kb.destination_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['destination_search_question']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "country_search")
async def country_search(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    menu = kb.country_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['country_search_question']
    await callback.message.answer(text=msg_text, reply_markup=menu)


@router.callback_query(F.data == "country_of_city_search")
async def country_of_city_search(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    menu = kb.country_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['country_search_question']
    await callback.message.answer(text=msg_text, reply_markup=menu)


class VisaAdvisory(StatesGroup):
    citizenship = State()
    destination = State()


@router.message(VisaAdvisory.citizenship)
async def inputCitizenship(msg: Message, state: FSMContext) -> None:
    await state.set_state(VisaAdvisory.destination)
    record = fetch_info(msg.chat.id)
    update_bd("citizenship", f"'{msg.text}'", msg.chat.id)

    msg_text = text.questionsVisa[f'{record[1]}']['destination']
    await msg.answer(text=msg_text)


@router.message(VisaAdvisory.destination)
async def inputDestination(msg: Message, state: FSMContext) -> None:
    update_bd("destination", f"'{msg.text}'", msg.chat.id)
    record = fetch_info(msg.from_user.id)
    result = visaAdvisory.visaAdvisory(record[2], record[3], record[1])
    await msg.answer(text=result)

@router.callback_query(F.data == "visa_advisory")
async def visa_advisory(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(VisaAdvisory.citizenship)
    record = fetch_info(callback.from_user.id)
    msg_text = text.questionsVisa[f'{record[1]}']['citizenship']
    await callback.message.answer(text=msg_text)



@router.message()
async def feedback(msg: Message):
    record = fetch_info(msg.chat.id)
    menu = kb.feedback_menu
    msg_text = text.questions[f'{record[1]}']['feedback']

    await msg.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "contact_experts")
async def contact_experts(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)

    menu = kb.experts_menu[f'{record[1]}']
    msg_text = text.cont_exp_quest[f'cont_exp_{record[1]}']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "lawyer")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['lawyer']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "tax_prof")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['tax_prof']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "real_estate_agent")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['real_estate_agent']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "relocation_buddy")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['relocation_buddy']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "immigration_adviser")
async def lawyer(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['immigration_adviser']
    await callback.message.answer(text=msg_text, reply_markup=menu)
