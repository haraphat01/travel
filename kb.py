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

destination_search_menu = [
    [InlineKeyboardButton(text="Country", callback_data="country_search"),
     InlineKeyboardButton(text="City", callback_data="country_of_city_search")]
]

country_search_menu = [
    [InlineKeyboardButton(text="Russia", callback_data="Russia"),
     InlineKeyboardButton(text="United States of America", callback_data="USA")],
    [InlineKeyboardButton(text="China", callback_data="China"),
     InlineKeyboardButton(text="Germany", callback_data="Germany")],
    [InlineKeyboardButton(text="France", callback_data="France"),
     InlineKeyboardButton(text="South Korea", callback_data="Korea")]
]

language_menu = InlineKeyboardMarkup(resize_keyboard = True, inline_keyboard=language)
menuRu = InlineKeyboardMarkup(inline_keyboard=russian_menu)
menuEng = InlineKeyboardMarkup(inline_keyboard=english_menu)

confirm_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_confirm_buttons)
confirm_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_confirm_buttons)

confirm_menu = {
    'ru': confirm_menu_ru,
    'eng': confirm_menu_eng
}

destination_search_menu = InlineKeyboardMarkup(inline_keyboard=destination_search_menu)
country_search_menu = InlineKeyboardMarkup(inline_keyboard=country_search_menu)


gender_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_gender_buttons)
gender_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_gender_buttons)

gender_menu = {
    'ru': gender_menu_ru,
    'eng': gender_menu_eng
}