from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import kb
import text
import db

router = Router()

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
    update = f"Update users set lang='ru' where id={callback.from_user.id}"
    db.cursor.execute(update)
    db.connect.commit()
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "eng")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.main_menu['menu_eng']
    menu = kb.menuEng
    update = f"Update users set lang='eng' where id={callback.from_user.id}"
    db.cursor.execute(update)
    db.connect.commit()
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "profile_search")
async def profile_search(callback: CallbackQuery):
    db.cursor.execute(f"Select * from users where id={callback.from_user.id}")
    record = db.cursor.fetchone()
    menu = kb.confirm_menu[f'{record[1]}']
    msg_text = text.questions[f'{record[1]}']['before_questions']
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "next")
async def questions(callback: CallbackQuery, state: FSMContext) -> None:
    db.cursor.execute(f"Select * from users where id={callback.from_user.id}")
    record = db.cursor.fetchone()

    msg_text = text.questions[f'{record[1]}']['age']
    await state.set_state(questions_for_profile_search.question1)
    await callback.message.answer(text=msg_text)

class questions_for_profile_search(StatesGroup):

    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    question6 = State()
    question7 = State()
    question8 = State()
    question9 = State()
    question10 = State()

@router.message(questions_for_profile_search.question1)
async def input_age(msg: Message, state: FSMContext) -> None:
    update = f"Update users set age={msg.text} where id={msg.chat.id}"
    db.cursor.execute(update)
    db.connect.commit()

    db.cursor.execute(f"Select * from users where id={msg.chat.id}")
    record = db.cursor.fetchone()

    msg_text = text.questions[f'{record[1]}']['gender']
    menu = kb.gender_menu[f'{record[1]}']
    await state.set_state(questions_for_profile_search.question2)
    await msg.answer(text=msg_text, reply_markup=menu)


@router.message(questions_for_profile_search.question2)
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

# text.greet.format(name=msg.from_user.full_name),
