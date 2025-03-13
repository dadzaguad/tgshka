import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import init_db, seed_data

TOKEN=os.getenv("TOKEN")



async def main():
    await init_db()
    await seed_data()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
