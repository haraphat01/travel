from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text="Choose the language: ", reply_markup=kb.language_menu)

@router.callback_query(F.data == "ru")
async def language_confirmation_ru(callback: CallbackQuery):
    msg_text = text.menuRu
    menu = kb.menuRu
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
    pass

# text.greet.format(name=msg.from_user.full_name),
