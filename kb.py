from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

edit_button_ru = [
    [InlineKeyboardButton(text="✍️Редактировать", callback_data="start_edit"),
     InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

edit_button_eng = [
    [InlineKeyboardButton(text="✍️Edit", callback_data="start_edit"),
     InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

edit_menu_ru = InlineKeyboardMarkup(inline_keyboard=edit_button_ru)
edit_menu_eng = InlineKeyboardMarkup(inline_keyboard=edit_button_eng)

edit_menu = {
    'ru': edit_menu_ru,
    'eng': edit_menu_eng
}

exit_button_ru = [
    [InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

exit_button_eng = [
     [InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

exit_menu_ru = InlineKeyboardMarkup(inline_keyboard=exit_button_ru)
exit_menu_eng = InlineKeyboardMarkup(inline_keyboard=exit_button_eng)

exit_menu = {
    'ru': exit_menu_ru,
    'eng': exit_menu_eng
}

confirm_edit_button_ru = [
    [InlineKeyboardButton(text="✅Подтвердить", callback_data="confirm_edit"),
     InlineKeyboardButton(text="❌Отмена", callback_data="admin")]
]

confirm_edit_button_eng = [
    [InlineKeyboardButton(text="✅Confirm", callback_data="confirm_edit"),
     InlineKeyboardButton(text="❌Cancel", callback_data="admin")]
]

confirm_edit_menu_ru = InlineKeyboardMarkup(inline_keyboard=confirm_edit_button_ru)
confirm_edit_menu_eng = InlineKeyboardMarkup(inline_keyboard=confirm_edit_button_eng)

confirm_edit_menu = {
    'ru': confirm_edit_menu_ru,
    'eng': confirm_edit_menu_eng
}


# Language selection
language_buttons = \
    [
        [InlineKeyboardButton(text="🇷🇺Russian", callback_data="ru"),
         InlineKeyboardButton(text="🇺🇸English", callback_data="eng")]
    ]

language_menu = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=language_buttons)

# Main menu for common user
english_menu_buttons = [
    [InlineKeyboardButton(text="🌍Destination Search", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Profile Search", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Visa Advisory", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Contact Experts", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Choose language", callback_data="language"),
     InlineKeyboardButton(text="🌟Leave feedback", callback_data="feedback")]
]

russian_menu_buttons = [
    [InlineKeyboardButton(text="🌍Поиск по месту назначения", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Поиск по параметрам", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Визовая консультация", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Связаться с экспертами", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Выбрать язык", callback_data="language"),
     InlineKeyboardButton(text="🌟Оставить отзыв", callback_data="feedback")]
]

menu_ru = InlineKeyboardMarkup(inline_keyboard=russian_menu_buttons)
menu_eng = InlineKeyboardMarkup(inline_keyboard=english_menu_buttons)

main_menu_buttons = {
    'ru': menu_ru,
    'eng': menu_eng
}

english_menu_with_experts_buttons = [
    [InlineKeyboardButton(text="🌍Destination Search", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Profile Search", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Visa Advisory", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Contact Experts", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Choose language", callback_data="language"),
     InlineKeyboardButton(text="🌟Leave feedback", callback_data="feedback")],
    [InlineKeyboardButton(text="🗓Check appointments", callback_data="check_appointments")]

]

russian_menu_with_experts_buttons = [
    [InlineKeyboardButton(text="🌍Поиск по месту назначения", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Поиск по параметрам", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Визовая консультация", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Связаться с экспертами", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Выбрать язык", callback_data="language"),
     InlineKeyboardButton(text="🌟Оставить отзыв", callback_data="feedback")],
    [InlineKeyboardButton(text="🗓Посмотреть записи", callback_data="check_appointments")]
]

menu_for_experts_ru = InlineKeyboardMarkup(inline_keyboard=russian_menu_with_experts_buttons)
menu_for_experts_eng = InlineKeyboardMarkup(inline_keyboard=english_menu_with_experts_buttons)

# Profile search confirm
profile_search_confirm_buttons_ru = [
    [InlineKeyboardButton(text="✅Давай", callback_data="next"),
     InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

profile_search_confirm_buttons_eng = [
    [InlineKeyboardButton(text="✅Let's start", callback_data="next"),
     InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

confirm_menu_ru = InlineKeyboardMarkup(inline_keyboard=profile_search_confirm_buttons_ru)
confirm_menu_eng = InlineKeyboardMarkup(inline_keyboard=profile_search_confirm_buttons_eng)

confirm_menu = {
    'ru': confirm_menu_ru,
    'eng': confirm_menu_eng
}

# Main menu for admin
eng_menu_admin_buttons = [
    [InlineKeyboardButton(text="🌍Destination Search", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Profile Search", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Visa Advisory", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Contact Experts", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Choose language", callback_data="language"),
     InlineKeyboardButton(text="🌟Leave feedback", callback_data="feedback")],
    [InlineKeyboardButton(text="⚙️Admin", callback_data="admin")]
]

ru_menu_admin_buttons = [
    [InlineKeyboardButton(text="🌍Поиск по месту назначения", callback_data="destination_search"),
     InlineKeyboardButton(text="🔍Поиск по параметрам", callback_data="profile_search")],
    [InlineKeyboardButton(text="🗺Визовая консультация", callback_data="visa_advisory"),
     InlineKeyboardButton(text="👨🏻‍🔬Связаться с экспертами", callback_data="contact_experts")],
    [InlineKeyboardButton(text="🇷🇺🇺🇸Выбрать язык", callback_data="language"),
     InlineKeyboardButton(text="🌟Оставить отзыв", callback_data="feedback")],
    [InlineKeyboardButton(text="⚙️Админ", callback_data="admin")]
]

admin_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_menu_admin_buttons)
admin_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_menu_admin_buttons)

admin_menu = {
    'ru': admin_menu_ru,
    'eng': admin_menu_eng
}

ru_admin_panel_buttons = [
    [InlineKeyboardButton(text="🆕Добавить город", callback_data="add_city"),
     InlineKeyboardButton(text="🆕Добавить эксперта", callback_data="add_expert")],
    [InlineKeyboardButton(text="✍️Отредактировать описание города", callback_data="edit_description")]
]

eng_admin_panel_buttons = [
    [InlineKeyboardButton(text="🆕Add new city", callback_data="add_city"),
     InlineKeyboardButton(text="🆕Add new expert", callback_data="add_expert")],
    [InlineKeyboardButton(text="✍️Edit description", callback_data="edit_description")]
]

admin_panel_ru = InlineKeyboardMarkup(inline_keyboard=ru_admin_panel_buttons)
admin_panel_eng = InlineKeyboardMarkup(inline_keyboard=eng_admin_panel_buttons)

admin_panel = {
    'ru': admin_panel_ru,
    'eng': admin_panel_eng
}

# Feedback
feedback_buttons = [
    [InlineKeyboardButton(text="⭐️", callback_data="1star"),
     InlineKeyboardButton(text="⭐️⭐️", callback_data="2stars")],
    [InlineKeyboardButton(text="⭐️⭐️⭐️", callback_data="3stars"),
     InlineKeyboardButton(text="⭐️⭐️⭐️⭐️", callback_data="4stars")],
    [InlineKeyboardButton(text="⭐️⭐️⭐️⭐️⭐️", callback_data="5stars")]
]

feedback_menu = InlineKeyboardMarkup(inline_keyboard=feedback_buttons)

# Destination search: menu
destination_search_menu_buttons_eng = [
    [InlineKeyboardButton(text="Country", callback_data="country_search"),
     InlineKeyboardButton(text="City", callback_data="country_of_city_search")]
]

destination_search_menu_buttons_ru = [
    [InlineKeyboardButton(text="Страна", callback_data="country_search"),
     InlineKeyboardButton(text="Город", callback_data="country_of_city_search")]
]

destination_search_menu_ru = InlineKeyboardMarkup(inline_keyboard=destination_search_menu_buttons_ru)
destination_search_menu_eng = InlineKeyboardMarkup(inline_keyboard=destination_search_menu_buttons_eng)

destination_menu = {
    'ru': destination_search_menu_ru,
    'eng': destination_search_menu_eng
}

# Destination search: country search
destination_search_country_search_menu_buttons_ru = [
    [InlineKeyboardButton(text="Россия", callback_data="Russia"),
     InlineKeyboardButton(text="Соединённые Штаты Америки", callback_data="USA")],
    [InlineKeyboardButton(text="Китай", callback_data="China"),
     InlineKeyboardButton(text="Германия", callback_data="Germany")],
    [InlineKeyboardButton(text="Франция", callback_data="France"),
     InlineKeyboardButton(text="Южная Корея", callback_data="Korea")]
]

destination_search_country_search_menu_buttons_eng = [
    [InlineKeyboardButton(text="Russia", callback_data="Russia"),
     InlineKeyboardButton(text="United States of America", callback_data="USA")],
    [InlineKeyboardButton(text="China", callback_data="China"),
     InlineKeyboardButton(text="Germany", callback_data="Germany")],
    [InlineKeyboardButton(text="France", callback_data="France"),
     InlineKeyboardButton(text="South Korea", callback_data="Korea")]
]

country_search_menu_ru = InlineKeyboardMarkup(inline_keyboard=destination_search_country_search_menu_buttons_ru)
country_search_menu_eng = InlineKeyboardMarkup(inline_keyboard=destination_search_country_search_menu_buttons_eng)

country_menu = {
    'ru': country_search_menu_ru,
    'eng': country_search_menu_eng
}

# Profile search: gender
ru_gender_buttons = [
    [InlineKeyboardButton(text="Женщина", callback_data="women"),
     InlineKeyboardButton(text="Мужчина", callback_data="man")]
]

eng_gender_buttons = [
    [InlineKeyboardButton(text="Woman", callback_data="women"),
     InlineKeyboardButton(text="Man", callback_data="man")],
]

gender_menu_ru = InlineKeyboardMarkup(inline_keyboard=ru_gender_buttons)
gender_menu_eng = InlineKeyboardMarkup(inline_keyboard=eng_gender_buttons)

gender_menu = {
    'ru': gender_menu_ru,
    'eng': gender_menu_eng
}

# Profile search: age
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

age_menu_ru = InlineKeyboardMarkup(inline_keyboard=age_buttons_ru)
age_menu_eng = InlineKeyboardMarkup(inline_keyboard=age_buttons_eng)

age_menu = {
    'ru': age_menu_ru,
    'eng': age_menu_eng
}

# Profile search: budget
budget_buttons_eng = [
    [InlineKeyboardButton(text="💰$500 - $2K/person", callback_data="1k")],
    [InlineKeyboardButton(text="💰$2K - $8K/person", callback_data="1-3k")],
    [InlineKeyboardButton(text="💰$8K/person and higher", callback_data="3k")]
]

budget_buttons_ru = [
    [InlineKeyboardButton(text="💰₽40K - ₽200K/человек", callback_data="1k")],
    [InlineKeyboardButton(text="💰₽200K - ₽700K/человек", callback_data="1-3k")],
    [InlineKeyboardButton(text="💰₽700K/человек и выше", callback_data="3k")]
]

budget_menu_eng = InlineKeyboardMarkup(inline_keyboard=budget_buttons_eng)
budget_menu_ru = InlineKeyboardMarkup(inline_keyboard=budget_buttons_ru)

budget_menu = {
    'ru': budget_menu_ru,
    'eng': budget_menu_eng
}

# Profile search: citizenship
citizenship_buttons_ru = [
    [InlineKeyboardButton(text="🇺🇸США", callback_data="usa"),
     InlineKeyboardButton(text="🇷🇺Россия", callback_data="russia")],
    [InlineKeyboardButton(text="🇮🇱Израиль", callback_data="israel"),
     InlineKeyboardButton(text="🇪🇺Евросоюз", callback_data="eu")],
    [InlineKeyboardButton(text="🇺🇦Украина", callback_data="ukraine"),
     InlineKeyboardButton(text="🇰🇿Казахстан", callback_data="kazah")],
    [InlineKeyboardButton(text="🇦🇲Армения", callback_data="armenia"),
     InlineKeyboardButton(text="🇬🇪Грузия", callback_data="georgia")],
    # [InlineKeyboardButton(text="Другое", callback_data="other_country")]
]

citizenship_buttons_eng = [
    [InlineKeyboardButton(text="🇺🇸USA", callback_data="usa"),
     InlineKeyboardButton(text="🇷🇺Russia", callback_data="russia")],
    [InlineKeyboardButton(text="🇮🇱Israel", callback_data="israel"),
     InlineKeyboardButton(text="🇪🇺EU", callback_data="eu")],
    [InlineKeyboardButton(text="🇺🇦Ukraine", callback_data="ukraine"),
     InlineKeyboardButton(text="🇰🇿Kazakhstan", callback_data="kazah")],
    [InlineKeyboardButton(text="🇦🇲Armenia", callback_data="armenia"),
     InlineKeyboardButton(text="🇬🇪Georgia", callback_data="georgia")],
    # [InlineKeyboardButton(text="Other", callback_data="other_country")]
]

citizenship_menu_ru = InlineKeyboardMarkup(inline_keyboard=citizenship_buttons_ru)
citizenship_menu_eng = InlineKeyboardMarkup(inline_keyboard=citizenship_buttons_eng)

citizenship_menu = {
    'ru': citizenship_menu_ru,
    'eng': citizenship_menu_eng
}

# Profile search: alone or with family
buttons_alone_family_ru = [
    [InlineKeyboardButton(text="🧍‍♂️Один", callback_data="alone"),
     InlineKeyboardButton(text="👨‍👩‍👦С семьей", callback_data="family")]
]

buttons_alone_family_eng = [
    [InlineKeyboardButton(text="🧍‍♂️Alone", callback_data="alone"),
     InlineKeyboardButton(text="👨‍👩‍👦With family", callback_data="family")]
]

alone_family_ru = InlineKeyboardMarkup(inline_keyboard=buttons_alone_family_ru)
alone_family_eng = InlineKeyboardMarkup(inline_keyboard=buttons_alone_family_eng)

alone_or_family = {
    'ru': alone_family_ru,
    'eng': alone_family_eng
}

# Profile search: climate
climate_buttons_eng = [
    [InlineKeyboardButton(text="Equatorial", callback_data="equatorial"),
     InlineKeyboardButton(text="Tropical", callback_data="tropical")],
    [InlineKeyboardButton(text="Polar", callback_data="polar")]
]

climate_buttons_ru = [
    [InlineKeyboardButton(text="Экваториальный", callback_data="equatorial"),
     InlineKeyboardButton(text="Тропический", callback_data="tropical")],
    [InlineKeyboardButton(text="Полярный", callback_data="polar")]
]

climate_menu_ru = InlineKeyboardMarkup(inline_keyboard=climate_buttons_ru)
climate_menu_eng = InlineKeyboardMarkup(inline_keyboard=climate_buttons_eng)

climate_menu = {
    'ru': climate_menu_ru,
    'eng': climate_menu_eng
}

# Profile search: motive
motive_buttons_ru = [
    [InlineKeyboardButton(text="🤴Бизнес", callback_data="business"),
     InlineKeyboardButton(text="⛵️Путешествие", callback_data="adventure")],
    [InlineKeyboardButton(text="📈Карьера", callback_data="career"),
     InlineKeyboardButton(text="👨‍👩‍👧Семейные обстоятельства", callback_data="family_op")],
    [InlineKeyboardButton(text="🗣Другое", callback_data="other_motive")]
]

motive_buttons_eng = [
    [InlineKeyboardButton(text="🤴Business", callback_data="business"),
     InlineKeyboardButton(text="⛵️Adventure", callback_data="adventure")],
    [InlineKeyboardButton(text="📈Career", callback_data="career"),
     InlineKeyboardButton(text="👨‍👩‍👧Family", callback_data="family_op")],
    [InlineKeyboardButton(text="🗣Other", callback_data="other_motive")]
]

motive_menu_ru = InlineKeyboardMarkup(inline_keyboard=motive_buttons_ru)
motive_menu_eng = InlineKeyboardMarkup(inline_keyboard=motive_buttons_eng)

relocation_motive_menu = {
    'ru': motive_menu_ru,
    'eng': motive_menu_eng
}

# Profile search: destination
destination_buttons_ru = [
    [InlineKeyboardButton(text="✅Да", callback_data="yes"),
     InlineKeyboardButton(text="❌Нет", callback_data="no")]
]

destination_buttons_eng = [
    [InlineKeyboardButton(text="✅Yes", callback_data="yes"),
     InlineKeyboardButton(text="❌No", callback_data="no")]
]

dest_menu_ru = InlineKeyboardMarkup(inline_keyboard=destination_buttons_ru)
dest_menu_eng = InlineKeyboardMarkup(inline_keyboard=destination_buttons_eng)

destination_res = {
    'ru': dest_menu_ru,
    'eng': dest_menu_eng
}

# Contact experts: menu
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

# Profile search: language
new_lang_buttons_ru = [
    [InlineKeyboardButton(text="✅Да", callback_data="yes_lang"),
     InlineKeyboardButton(text="❌Нет", callback_data="no_lang")]
]

new_lang_buttons_eng = [
    [InlineKeyboardButton(text="✅Yes", callback_data="yes_lang"),
     InlineKeyboardButton(text="❌No", callback_data="no_lang")]
]

lang_menu_ru = InlineKeyboardMarkup(inline_keyboard=new_lang_buttons_ru)
lang_menu_eng = InlineKeyboardMarkup(inline_keyboard=new_lang_buttons_eng)

lang_menu = {
    'ru': lang_menu_ru,
    'eng': lang_menu_eng
}

# Profile search: priorities
priorities_buttons_ru = [
    [InlineKeyboardButton(text="🏥Здравоохранение", callback_data="health_system"),
     InlineKeyboardButton(text="🏫Образование", callback_data="education")],
    [InlineKeyboardButton(text="🌳Природа", callback_data="nature"),
     InlineKeyboardButton(text="🥂Развлечения", callback_data="city_life")],
    [InlineKeyboardButton(text="🏘️Инфраструктура", callback_data="infrastructure")]
]

priorities_buttons_eng = [
    [InlineKeyboardButton(text="🏥Health system", callback_data="health_system"),
     InlineKeyboardButton(text="🏫Education", callback_data="education")],
    [InlineKeyboardButton(text="🌳Nature", callback_data="nature"),
     InlineKeyboardButton(text="🥂City life", callback_data="city_life")],
    [InlineKeyboardButton(text="🏘️Infrastructure", callback_data="infrastructure")]
]

priorities_menu_ru = InlineKeyboardMarkup(inline_keyboard=priorities_buttons_ru)
priorities_menu_eng = InlineKeyboardMarkup(inline_keyboard=priorities_buttons_eng)

priorities_menu = {
    'ru': priorities_menu_ru,
    'eng': priorities_menu_eng
}

# Profile search: population
population_buttons_ru = [
    [InlineKeyboardButton(text="🤏Маленький(<150K человек)", callback_data="population_150k"),
     InlineKeyboardButton(text="🏠Средний(>200K человек)", callback_data="population_200k")],
    [InlineKeyboardButton(text="🏙Большой(>1000K человек)", callback_data="population_500k")]
]

population_buttons_eng = [
    [InlineKeyboardButton(text="🤏Small(<150K people)", callback_data="population_150k"),
     InlineKeyboardButton(text="🏠Medium(>200K people)", callback_data="population_200k")],
    [InlineKeyboardButton(text="🏙Big(>1000K people)", callback_data="population_500k")]
]

population_menu_ru = InlineKeyboardMarkup(inline_keyboard=population_buttons_ru)
population_menu_eng = InlineKeyboardMarkup(inline_keyboard=population_buttons_eng)

population_menu = {
    'ru': population_menu_ru,
    'eng': population_menu_eng
}

# Profile search: neighbours
neighbours_buttons_ru = [
    [InlineKeyboardButton(text="🥳Дружелюбные", callback_data="spicy"),
     InlineKeyboardButton(text="😐Нормальные", callback_data="normal")],
    [InlineKeyboardButton(text="😶Безразлично", callback_data="indifferent")]
]

neighbours_buttons_eng = [
    [InlineKeyboardButton(text="🥳Spicy", callback_data="spicy"),
     InlineKeyboardButton(text="😐Warm", callback_data="normal")],
    [InlineKeyboardButton(text="😶Cold", callback_data="indifferent")]
]

neighbours_menu_ru = InlineKeyboardMarkup(inline_keyboard=neighbours_buttons_ru)
neighbours_menu_eng = InlineKeyboardMarkup(inline_keyboard=neighbours_buttons_eng)

neighbours_menu = {
    'ru': neighbours_menu_ru,
    'eng': neighbours_menu_eng
}

# Contact experts: options
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

english_date_schedule = [
    [InlineKeyboardButton(text="10 a.m.", callback_data="ten"),
     InlineKeyboardButton(text="11 a.m.", callback_data="eleven")],
    [InlineKeyboardButton(text="12 p.m.", callback_data="twelve"),
     InlineKeyboardButton(text="1 p.m.", callback_data="thirteen")],
    [InlineKeyboardButton(text="2 p.m.", callback_data="fourteen"),
     InlineKeyboardButton(text="3 p.m.", callback_data="fifteen")],
    [InlineKeyboardButton(text="4 p.m.", callback_data="sixteen"),
     InlineKeyboardButton(text="5 p.m.", callback_data="seventeen")],
    [InlineKeyboardButton(text="6 p.m.", callback_data="eighteen")]
]

russian_date_schedule = [
    [InlineKeyboardButton(text="10:00", callback_data="ten"),
     InlineKeyboardButton(text="11:00", callback_data="eleven")],
    [InlineKeyboardButton(text="12:00", callback_data="twelve"),
     InlineKeyboardButton(text="13:00", callback_data="thirteen")],
    [InlineKeyboardButton(text="14:00", callback_data="fourteen"),
     InlineKeyboardButton(text="15:00", callback_data="fifteen")],
    [InlineKeyboardButton(text="16:00", callback_data="sixteen"),
     InlineKeyboardButton(text="17:00", callback_data="seventeen")],
    [InlineKeyboardButton(text="18:00", callback_data="eighteen")]
]

schedule_dates_eng = InlineKeyboardMarkup(inline_keyboard=english_date_schedule)
schedule_dates_ru = InlineKeyboardMarkup(inline_keyboard=russian_date_schedule)

date_schedule = {
    'ru': schedule_dates_ru,
    'eng': schedule_dates_eng
}



# Next City
ru_next_city = [
    [InlineKeyboardButton(text="✅Следующий город", callback_data="next_city")],
    [InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

eng_next_city = [
    [InlineKeyboardButton(text="✅Next city", callback_data="next_city")],
    [InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

ru_city_menu = InlineKeyboardMarkup(inline_keyboard=ru_next_city)
eng_city_menu = InlineKeyboardMarkup(inline_keyboard=eng_next_city)

city_menu = {
    'ru': ru_city_menu,
    'eng': eng_city_menu
}

ru_main = [
    [InlineKeyboardButton(text="❌Главное меню", callback_data="ru")]
]

eng_main = [
    [InlineKeyboardButton(text="❌Main menu", callback_data="eng")]
]

ru_main_menu = InlineKeyboardMarkup(inline_keyboard=ru_main)
eng_main_menu = InlineKeyboardMarkup(inline_keyboard=eng_main)

main_menu = {
    'ru': ru_main_menu,
    'eng': eng_main_menu
}
back_eng = [
    [InlineKeyboardButton(text="Try again", callback_data="visa_advisory"),
     InlineKeyboardButton(text="Return to menu", callback_data="eng")
     ]
]
back_ru = [
    [InlineKeyboardButton(text="Попробовать еще раз", callback_data="visa_advisory"),
     InlineKeyboardButton(text="Вернуться в меню", callback_data="ru")]
]
back_menu_ru = InlineKeyboardMarkup(inline_keyboard=back_ru)
back_menu_eng = InlineKeyboardMarkup(inline_keyboard=back_eng)
back_menu = {
    'ru': back_menu_ru,
    'eng': back_menu_eng
}

visaFeedback_ru = [
    [InlineKeyboardButton(text="Оставить отзыв", callback_data="visa_feedback"),
        InlineKeyboardButton(text="Вернуться в меню", callback_data="ru")]
]
visaFeedback_eng = [
    [InlineKeyboardButton(text="Leave feedback", callback_data="visa_feedback"),
        InlineKeyboardButton(text="Return to menu", callback_data="eng")]
]
visaFeedback_menu_ru = InlineKeyboardMarkup(inline_keyboard=visaFeedback_ru)
visaFeedback_menu_eng = InlineKeyboardMarkup(inline_keyboard=visaFeedback_eng)
visaFeedback_menu = {
    'ru': visaFeedback_menu_ru,
    'eng': visaFeedback_menu_eng
}