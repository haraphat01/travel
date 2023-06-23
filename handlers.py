from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import kb
import text
import db

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
    menu = kb.menuRu
    update_bd('lang', "'ru'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "eng")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
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
async def questions(callback: CallbackQuery, state: FSMContext) -> None:
    record = fetch_info(callback.from_user.id)

    msg_text = text.questions[f'{record[1]}']['age']
    await state.set_state(questions_for_profile_search.age)
    await callback.message.answer(text=msg_text)

class questions_for_profile_search(StatesGroup):

    age = State()
    gender = State()
    budget = State()
    citizenship = State()
    relocation_motive = State()
    climate = State()
    city_size = State()
    continent = State()
    medicine_level = State()
    education_level = State()

@router.message(questions_for_profile_search.age)
async def input_age(msg: Message, state: FSMContext) -> None:
    update = f"Update users set age={msg.text} where id={msg.chat.id}"
    db.cursor.execute(update)
    db.connect.commit()

    record = fetch_info(msg.chat.id)

    msg_text = text.questions[f'{record[1]}']['gender']
    menu = kb.gender_menu[f'{record[1]}']
    await state.set_state(questions_for_profile_search.gender)
    await msg.answer(text=msg_text, reply_markup=menu)


@router.message(questions_for_profile_search.gender)
async def input_gender(msg: Message, state: FSMContext) -> None:
    await state.update_data(gender=msg.text)
    await state.set_state(questions_for_profile_search.question3)
    await msg.answer(text="Теперь выбери свой пол", reply_markup=kb.gender_menu_ru)

@router.callback_query(F.data == "language")
async def language_selection(callback: CallbackQuery):
    await callback.message.answer(text="Choose the language: ", reply_markup=kb.language_menu)


@router.callback_query(F.data == "destination_search")
async def destination_search(callback: CallbackQuery):
    await callback.message.answer(text=text.destination_search_question, reply_markup=kb.destination_search_menu)


@router.callback_query(F.data == "country_search")
async def country_search(callback: CallbackQuery):
    await callback.message.answer(text=text.country_search_question, reply_markup=kb.country_search_menu)


@router.callback_query(F.data == "country_of_city_search")
async def country_of_city_search(callback: CallbackQuery):
    await callback.message.answer(text=text.country_of_city_search_question, reply_markup=kb.country_search_menu)


@router.callback_query(F.data == "visa_advisory")
async def visa_advisory(callback: CallbackQuery):
    pass

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
    update_bd('experts', "'lawyer'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "tax_prof")
async def tax_prof(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['tax_prof']
    update_bd('experts', "'tax_prof'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "real_estate_agent")
async def real_estate_agent(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['real_estate_agent']
    update_bd('experts', "'real_estate_agent'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "relocation_buddy")
async def relocation_buddy(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['relocation_buddy']
    update_bd('experts', "'relocation_buddy'", callback.from_user.id)
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "immigration_adviser")
async def immigration_adviser(callback: CallbackQuery):
    record = fetch_info(callback.from_user.id)
    menu = kb.experts_options[f'{record[1]}']
    msg_text = text.experts_menu[f'{record[1]}']['immigration_adviser']
    update_bd('experts', "'immigration_adviser'", callback.from_user.id)
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
    msg_text = text.booking_menu[f'{record[1]}'][f'expert_{record[13]}']
    await callback.message.answer(text=msg_text)


# text.greet.format(name=msg.from_user.full_name),
