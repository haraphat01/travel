from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
english_menu = [
    [InlineKeyboardButton(text="🌍Destination Search", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Profile Search", callback_data="profile_search")],
     [InlineKeyboardButton(text="🗺Visa Advisory", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Contact Experts", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Choose language", callback_data="language")]
]

russian_menu = [
    [InlineKeyboardButton(text="🌍Поиск по месту назначения", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Поиск по параметрам", callback_data="profile_search")],
     [InlineKeyboardButton(text="🗺Визовая консультация", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Связаться с экспертами", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Выбрать язык", callback_data="language")]
]

eng_menu_admin = [
    [InlineKeyboardButton(text="🌍Destination Search", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Profile Search", callback_data="profile_search")],
     [InlineKeyboardButton(text="🗺Visa Advisory", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Contact Experts", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Choose language", callback_data="language")],
    [InlineKeyboardButton(text="⚙️Admin", callback_data="admin")]
]

ru_menu_admin = [
    [InlineKeyboardButton(text="🌍Поиск по месту назначения", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Поиск по параметрам", callback_data="profile_search")],
     [InlineKeyboardButton(text="🗺Визовая консультация", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Связаться с экспертами", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Выбрать язык", callback_data="language")],
    [InlineKeyboardButton(text="⚙️Админ", callback_data="admin")]
]

feedback_buttons = [
    [InlineKeyboardButton(text="⭐️", callback_data="1star"),
     InlineKeyboardButton(text="⭐️⭐️", callback_data="2stars")],
    [InlineKeyboardButton(text="⭐️⭐️⭐️", callback_data="3stars"),
     InlineKeyboardButton(text="⭐️⭐️⭐️⭐️", callback_data="4stars")],
    [InlineKeyboardButton(text="⭐️⭐️⭐️⭐️⭐️", callback_data="5stars")]
]

feedback_menu = InlineKeyboardMarkup(inline_keyboard=feedback_buttons)

admin_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_menu_admin)
admin_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_menu_admin)

language = \
[
    [InlineKeyboardButton(text="🇷🇺Russian", callback_data="ru"),
     InlineKeyboardButton(text="🇺🇸English", callback_data="eng")]
]


ru_confirm_buttons = [
    [InlineKeyboardButton(text="✅Давай", callback_data="next"),
     InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

eng_confirm_buttons = [
    [InlineKeyboardButton(text="✅Let's start", callback_data="next"),
     InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

ru_gender_buttons = [
    [InlineKeyboardButton(text="Женщина", callback_data="women"),
     InlineKeyboardButton(text="Мужчина", callback_data="man")],
    [InlineKeyboardButton(text="Другое", callback_data="other")]
]

eng_gender_buttons = [
    [InlineKeyboardButton(text="Woman", callback_data="women"),
     InlineKeyboardButton(text="Man", callback_data="man")],
    [InlineKeyboardButton(text="Other", callback_data="other")]
]

destination_search_menu_buttons_eng = [
    [InlineKeyboardButton(text="Country", callback_data="country_search"),
     InlineKeyboardButton(text="City", callback_data="country_of_city_search")]
]

destination_search_menu_buttons_ru = [
    [InlineKeyboardButton(text="Страна", callback_data="country_search"),
     InlineKeyboardButton(text="Город", callback_data="country_of_city_search")]
]

country_search_menu_buttons_ru = [
    [InlineKeyboardButton(text="Россия", callback_data="Russia"),
     InlineKeyboardButton(text="Соединённые Штаты Америки", callback_data="USA")],
    [InlineKeyboardButton(text="Китай", callback_data="China"),
     InlineKeyboardButton(text="Германия", callback_data="Germany")],
    [InlineKeyboardButton(text="Франция", callback_data="France"),
     InlineKeyboardButton(text="Южная Корея", callback_data="Korea")]
]

country_search_menu_buttons_eng = [
    [InlineKeyboardButton(text="Russia", callback_data="Russia"),
     InlineKeyboardButton(text="United States of America", callback_data="USA")],
    [InlineKeyboardButton(text="China", callback_data="China"),
     InlineKeyboardButton(text="Germany", callback_data="Germany")],
    [InlineKeyboardButton(text="France", callback_data="France"),
     InlineKeyboardButton(text="South Korea", callback_data="Korea")]
]

age_buttons_ru = [
    [InlineKeyboardButton(text="<14", callback_data="<14"),
     InlineKeyboardButton(text="14 - 18", callback_data=">14<18")],
    [InlineKeyboardButton(text="18 - 30", callback_data=">18<30"),
     InlineKeyboardButton(text=">30", callback_data="<30")]
]

age_buttons_eng = [
    [InlineKeyboardButton(text="<14", callback_data="<14"),
     InlineKeyboardButton(text="14 - 18", callback_data=">14<18")],
    [InlineKeyboardButton(text="18 - 30", callback_data=">18<30"),
     InlineKeyboardButton(text=">30", callback_data="<30")]
]

language_menu = InlineKeyboardMarkup(resize_keyboard = True, inline_keyboard=language)
menuRu = InlineKeyboardMarkup(inline_keyboard=russian_menu)
menuEng = InlineKeyboardMarkup(inline_keyboard=english_menu)

confirm_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_confirm_buttons)
confirm_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_confirm_buttons)

age_menu_ru = InlineKeyboardMarkup(inline_keyboard=age_buttons_ru)
age_menu_eng = InlineKeyboardMarkup(inline_keyboard=age_buttons_eng)

budget_buttons_eng = [
    [InlineKeyboardButton(text="<$2K/person", callback_data="1k")],
    [InlineKeyboardButton(text="$2K - $5K/person", callback_data="2-5k")],
    [InlineKeyboardButton(text=">$5K/person", callback_data="5k")]
]

budget_buttons_ru = [
    [InlineKeyboardButton(text="<$2K/человек", callback_data="1k")],
    [InlineKeyboardButton(text="$2K - $5K/человек", callback_data="2-5k")],
    [InlineKeyboardButton(text=">$5K/человек", callback_data="5k")]
]

citizenship_buttons_ru = [
    [InlineKeyboardButton(text="США", callback_data="usa"),
     InlineKeyboardButton(text="Россия", callback_data="russia")],
    [InlineKeyboardButton(text="Израиль", callback_data="israel"),
     InlineKeyboardButton(text="Евросоюз", callback_data="eu")],
    [InlineKeyboardButton(text="Украина", callback_data="ukraine"),
     InlineKeyboardButton(text="Казахстан", callback_data="kazah")],
    [InlineKeyboardButton(text="Армения", callback_data="armenia"),
     InlineKeyboardButton(text="Грузия", callback_data="georgia")],
    [InlineKeyboardButton(text="Другое", callback_data="other_country")]
]

citizenship_buttons_eng = [
    [InlineKeyboardButton(text="USA", callback_data="usa"),
     InlineKeyboardButton(text="Russia", callback_data="russia")],
    [InlineKeyboardButton(text="Israel", callback_data="israel"),
     InlineKeyboardButton(text="EU", callback_data="eu")],
    [InlineKeyboardButton(text="Ukraine", callback_data="ukraine"),
     InlineKeyboardButton(text="Kazakhstan", callback_data="kazah")],
    [InlineKeyboardButton(text="Armenia", callback_data="armenia"),
     InlineKeyboardButton(text="Georgia", callback_data="georgia")],
    [InlineKeyboardButton(text="Other", callback_data="other_country")]
]

climate_buttons_eng = [
    [InlineKeyboardButton(text="❄️Cold", callback_data="cold"),
     InlineKeyboardButton(text="☁️Windy", callback_data="windy")],
    [InlineKeyboardButton(text="☀️Hot", callback_data="hot")]
]

climate_buttons_ru = [
    [InlineKeyboardButton(text="❄️Холодно", callback_data="cold"),
     InlineKeyboardButton(text="☁️Ветрено", callback_data="windy")],
    [InlineKeyboardButton(text="☀️Жарко", callback_data="hot")]
]

motive_buttons_ru = [
    [InlineKeyboardButton(text="🤴Бизнес", callback_data="business"),
     InlineKeyboardButton(text="⛵️Путешествие", callback_data="adventure")],
    [InlineKeyboardButton(text="📈Карьера", callback_data="career"),
     InlineKeyboardButton(text="👨‍👩‍👧Семейные обстоятельства", callback_data="family")],
    [InlineKeyboardButton(text="🗣Другое", callback_data="other_motive")]
]

motive_buttons_eng = [
    [InlineKeyboardButton(text="🤴Business", callback_data="business"),
     InlineKeyboardButton(text="⛵️Adventure", callback_data="adventure")],
    [InlineKeyboardButton(text="📈Career", callback_data="career"),
     InlineKeyboardButton(text="👨‍👩‍👧Family", callback_data="family")],
    [InlineKeyboardButton(text="🗣Other", callback_data="other_motive")]
]


citizenship_menu_ru = InlineKeyboardMarkup(inline_keyboard=citizenship_buttons_ru)
citizenship_menu_eng = InlineKeyboardMarkup(inline_keyboard=citizenship_buttons_eng)

citizenship_menu = {
    'ru': citizenship_menu_ru,
    'eng': citizenship_menu_eng
}

budget_menu_eng = InlineKeyboardMarkup(inline_keyboard=budget_buttons_eng)
budget_menu_ru = InlineKeyboardMarkup(inline_keyboard=budget_buttons_ru)

budget_menu = {
    'ru': budget_menu_ru,
    'eng': budget_menu_eng
}

age_menu = {
    'ru': age_menu_ru,
    'eng': age_menu_eng
}

confirm_menu = {
    'ru': confirm_menu_ru,
    'eng': confirm_menu_eng
}

destination_search_menu_ru = InlineKeyboardMarkup(inline_keyboard=destination_search_menu_buttons_ru)
destination_search_menu_eng = InlineKeyboardMarkup(inline_keyboard=destination_search_menu_buttons_eng)

destination_menu = {
    'ru': destination_search_menu_ru,
    'eng': destination_search_menu_eng
}

country_search_menu_ru = InlineKeyboardMarkup(inline_keyboard=country_search_menu_buttons_ru)
country_search_menu_eng = InlineKeyboardMarkup(inline_keyboard=country_search_menu_buttons_eng)

country_menu = {
    'ru': country_search_menu_ru,
    'eng': country_search_menu_eng
}


gender_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_gender_buttons)
gender_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_gender_buttons)

gender_menu = {
    'ru': gender_menu_ru,
    'eng': gender_menu_eng
}

climate_menu_ru = InlineKeyboardMarkup(inline_keyboard=climate_buttons_ru)
climate_menu_eng = InlineKeyboardMarkup(inline_keyboard=climate_buttons_eng)

climate_menu = {
    'ru': climate_menu_ru,
    'eng': climate_menu_eng
}

motive_menu_ru = InlineKeyboardMarkup(inline_keyboard=motive_buttons_ru)
motive_menu_eng = InlineKeyboardMarkup(inline_keyboard=motive_buttons_eng)

relocation_motive_menu = {
    'ru': motive_menu_ru,
    'eng': motive_menu_eng
}

english_experts_menu = [
    [InlineKeyboardButton(text="Lawyer", callback_data="lawyer"),
     InlineKeyboardButton(text="Tax professional", callback_data="tax_prof"),
    InlineKeyboardButton(text="Real estate agent", callback_data="real_estate_agent")],
    [InlineKeyboardButton(text="Relocation buddy", callback_data="relocation_buddy")],
     [InlineKeyboardButton(text="Immigration adviser", callback_data="immigration_adviser")]
]

russian_experts_menu = [
    [InlineKeyboardButton(text="Адвокат", callback_data="lawyer"),
     InlineKeyboardButton(text="Специалист по налогообложению", callback_data="tax_prof"),
    InlineKeyboardButton(text="Агент по недвижимости", callback_data="real_estate_agent")],
     [InlineKeyboardButton(text="Помощник по переезду", callback_data="relocation_buddy")],
     [InlineKeyboardButton(text="Иммиграционный советник", callback_data="immigration_adviser")]
     ]

experts_menu_eng = InlineKeyboardMarkup(inline_keyboard=english_experts_menu)
experts_menu_ru = InlineKeyboardMarkup(inline_keyboard=russian_experts_menu)

experts_menu = {
    'ru': experts_menu_ru,
    'eng': experts_menu_eng
}

english_experts_options = [
    [InlineKeyboardButton(text="✅Book appointment", callback_data="book_appointment"),
     InlineKeyboardButton(text="❌Cancel", callback_data="cancel")]
]

russian_experts_options = [
    [InlineKeyboardButton(text="✅Запись на прием", callback_data="book_appointment"),
     InlineKeyboardButton(text="❌Отмена", callback_data="cancel")]
]

experts_options_eng = InlineKeyboardMarkup(inline_keyboard=english_experts_options)
experts_options_ru = InlineKeyboardMarkup(inline_keyboard=russian_experts_options)

experts_options = {
    'ru': experts_options_ru,
    'eng': experts_options_eng
}