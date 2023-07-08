import kb
import handlers


import pytest

from aiogram_tests import MockedBot
import aiogram.utils
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE


@pytest.mark.asyncio
async def test_echo():
    request = MockedBot(MessageHandler(handlers.start_handler))
    calls = await request.query(message=MESSAGE.as_object(text="Choose the language: ", reply_markup=kb.language_menu))
    answer_message = calls.send_messsage.fetchone()
    assert answer_message.text == "Choose the language: "
