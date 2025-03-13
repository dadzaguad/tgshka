import pytest
from app import keyboards

@pytest.mark.asyncio
async def test_categories_keyboard():
    """
    Тестирует функцию создания клавиатуры с категориями товаров.
    Проверяет, что клавиатура создается и содержит кнопки категорий.
    """
    keyboard = await keyboards.categories()
    assert keyboard is not None
    assert len(keyboard.inline_keyboard) > 0

@pytest.mark.asyncio
async def test_items_keyboard():
    """
    Тестирует функцию создания клавиатуры с товарами из заданной категории.
    Проверяет, что клавиатура создается и содержит кнопки товаров.
    """
    keyboard = await keyboards.items(1)
    assert keyboard is not None
    assert len(keyboard.inline_keyboard) > 0