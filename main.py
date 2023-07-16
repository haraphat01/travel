import asyncio
import sqlite3
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router
from admin import bot

# bot = Bot(token=config.BOT_TEST_TOKEN, parse_mode=ParseMode.HTML)


async def update_columns(db_column):
    try:
        conn = sqlite3.connect('users.db')
        db = conn.cursor()
        db.execute(f"UPDATE users SET {db_column} = 'NULL'")
        conn.commit()
        conn.close()
        print('Columns updated successfully!')
    except Exception as e:
        print('Error updating columns:', e)


async def main():
    # bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    # while True:
    #     await asyncio.sleep(10)
    #     await update_columns('ten')
    #     await update_columns('eleven')
    #     await update_columns('twelve')
    #     await update_columns('thirteen')
    #     await update_columns('fourteen')
    #     await update_columns('fifteen')
    #     await update_columns('sixteen')
    #     await update_columns('seventeen')
    #     await update_columns('eighteen')
    # await sendNotification("test", '1703986509')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def sendNotification(msg: str, id: str):
    await bot.send_message(chat_id=id, text=msg)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
