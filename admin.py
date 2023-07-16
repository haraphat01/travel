from aiogram import Bot
import config
from aiogram.enums.parse_mode import ParseMode

bot = Bot(token=config.BOT_TEST_TOKEN, parse_mode=ParseMode.HTML)