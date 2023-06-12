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

ru_gender_buttons = [
    [InlineKeyboardButton(text="Женщина", callback_data="women"),
     InlineKeyboardButton(text="Мужчина", callback_data="man")],
    [InlineKeyboardButton(text="Другое", callback_data="other")]
]

language_menu = InlineKeyboardMarkup(resize_keyboard = True, inline_keyboard=language)

menuRu = InlineKeyboardMarkup(inline_keyboard=russian_menu)
menuEng = InlineKeyboardMarkup(inline_keyboard=english_menu)
confirm_menu = InlineKeyboardMarkup(inline_keyboard=ru_confirm_buttons)


gender_menu = InlineKeyboardMarkup(inline_keyboard=ru_gender_buttons)