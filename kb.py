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

destination_search_menu = [
    [InlineKeyboardButton(text="Country", callback_data="country_search"),
     InlineKeyboardButton(text="City", callback_data="city")]
]

language_menu = InlineKeyboardMarkup(resize_keyabord = True, inline_keyboard=language)

menuRu = InlineKeyboardMarkup(inline_keyboard=russian_menu)
menuEng = InlineKeyboardMarkup(inline_keyboard=english_menu)
destination_search_menu = InlineKeyboardMarkup(inline_keyboard=destination_search_menu)
