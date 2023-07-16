from admin import bot

async def notification(msg: str, id: str):
    await bot.send_message(chat_id=id, text=msg)