import pytest
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from unittest.mock import AsyncMock, MagicMock

from app.database.models import init_db, seed_data
from app.handlers import router

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def bot():
    bot = MagicMock(spec=Bot)
    bot.send_message = AsyncMock()
    bot.edit_message_text = AsyncMock()
    return bot

@pytest.fixture
def dp():
    dp = Dispatcher()
    dp.include_router(router)
    return dp

@pytest.fixture
def message(bot: MagicMock, dp: Dispatcher):
    message = MagicMock(spec=Message)
    message.bot = bot
    message.dp = dp
    message.from_user = MagicMock()
    message.chat = MagicMock()
    return message

@pytest.fixture
def callback_query(bot: MagicMock, dp: Dispatcher):
    callback_query = MagicMock(spec=CallbackQuery)
    callback_query.bot = bot
    callback_query.dp = dp
    callback_query.from_user = MagicMock()
    callback_query.message = MagicMock()
    callback_query.message.chat = MagicMock()
    return callback_query

@pytest.fixture(autouse=True)
async def setup_db():
    await init_db()
    await seed_data()