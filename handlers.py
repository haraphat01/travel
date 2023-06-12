from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import kb
import text
import db

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    user_id = [msg.chat.id]
    db.cursor.execute("INSERT INTO users(id) VALUES(?)", user_id)
    db.connect.commit()
    await msg.answer(text="Choose the language: ", reply_markup=kb.language_menu)

@router.callback_query(F.data == "ru")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.menuRu
    menu = kb.menuRu
    user_id = callback.from_user.id
    update = f"Update users set lang='ru' where id={user_id}"
    db.cursor.execute(update)
    db.connect.commit()
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "eng")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.menuEng
    menu = kb.menuEng
    await callback.message.answer(text=msg_text, reply_markup=menu)

@router.callback_query(F.data == "language")
async def language_selection(callback: CallbackQuery):
    await callback.message.answer(text="Choose the language: ", reply_markup=kb.language_menu)

@router.callback_query(F.data == "profile_search")
async def profile_search(callback: CallbackQuery):
    menu = kb.confirm_menu
    await callback.message.answer(text=text.before_questions, reply_markup=menu)

@router.callback_query(F.data == "destination_search")
async def destination_search(callback: CallbackQuery):
    pass

@router.callback_query(F.data == "visa_advisory")
async def visa_advisory(callback: CallbackQuery):
    pass

# text.greet.format(name=msg.from_user.full_name),
