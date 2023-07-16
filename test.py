from utils import division, summa
import kb
import handlers
import pytest
import notify

import text


@pytest.mark.asyncio
async def test_division():
    assert division(10, 2) == 5


@pytest.mark.asyncio
async def test_summa():
    assert summa(3, 2) == 5


@pytest.mark.asyncio
async def test_start_handler():
    assert handlers.start_handler("Choose the language: ")


@pytest.mark.asyncio
async def test_ru():
    assert handlers.language_confirmation_eng("Choose the language: ")


@pytest.mark.asyncio
async def test_eng():
    assert handlers.language_confirmation_eng("Choose the language: ")


@pytest.mark.asyncio
async def test_profile_search():
    assert handlers.profile_search(
        "Before I send you options for places you can move to, I need to ask a few questions.")


@pytest.mark.asyncio
async def test_next_handler():
    assert handlers.next("1. Input your gender", kb.gender_menu)


@pytest.mark.asyncio
async def test_women():
    assert handlers.women("2. Why do you want to move to another country?")


@pytest.mark.asyncio
async def test_man():
    assert handlers.man("2. Why do you want to move to another country?")


@pytest.mark.asyncio
async def test_less_2k():
    assert handlers.less_2k("3. What is your budget?")


@pytest.mark.asyncio
async def test_from_1_to_3():
    assert handlers.from_1_to_3("3. What is your budget?")


@pytest.mark.asyncio
async def test_greater_3k():
    assert handlers.from_1_to_3("3. What is your budget?")


@pytest.mark.asyncio
async def test_alone():
    assert handlers.alone("5. Have you decided where you want to relocate?")
