import pytest
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from unittest.mock import MagicMock, AsyncMock

@pytest.mark.asyncio
async def test_cmd_start(message: MagicMock, bot: MagicMock, dp: Dispatcher):
    """
    Тестирует обработчик команды /start.
    Проверяет, что бот отправляет приветственное сообщение при получении команды /start.
    """
    message.text = "/start"
    message.from_user.id = 12345
    await dp.feed_update(bot, message)
    bot.send_message.assert_called_once()
    assert bot.send_message.call_args[1]["text"].startswith("Добро пожаловать")

@pytest.mark.asyncio
async def test_catalog(message: MagicMock, bot: MagicMock, dp: Dispatcher):
    """
    Тестирует обработчик команды "Каталог".
    Проверяет, что бот отправляет сообщение с предложением выбрать категорию товара.
    """
    message.text = "Каталог"
    await dp.feed_update(bot, message)
    bot.send_message.assert_called_once()
    assert bot.send_message.call_args[1]["text"].startswith("Выберите категорию")

@pytest.mark.asyncio
async def test_category(callback_query: MagicMock, bot: MagicMock, dp: Dispatcher):
    """
    Тестирует обработчик выбора категории товара.
    Проверяет, что бот отправляет сообщение с предложением выбрать товар из выбранной категории.
    """
    callback_query.data = "category_1"
    await dp.feed_update(bot, callback_query)
    bot.send_message.assert_called()
    assert bot.send_message.call_args[1]["text"].startswith("Выберите товар")

@pytest.mark.asyncio
async def test_item(callback_query: MagicMock, bot: MagicMock, dp: Dispatcher):
    """
    Тестирует обработчик выбора товара.
    Проверяет, что бот отправляет сообщение с информацией о выбранном товаре.
    """
    callback_query.data = "item_1"
    await dp.feed_update(bot, callback_query)
    bot.send_message.assert_called()
    assert bot.send_message.call_args[1]["text"].startswith("Название:")