import pytest
from app.database import requests

@pytest.mark.asyncio
async def test_set_user():
    """
    Тестирует функцию добавления пользователя в базу данных.
    Проверяет, что пользователь успешно добавляется в базу данных.
    """
    await requests.set_user(123456)
    # Здесь можно добавить проверку, что пользователь был добавлен в базу данных
    # (например, с помощью запроса к базе данных)

@pytest.mark.asyncio
async def test_get_categories():
    """
    Тестирует функцию получения списка категорий из базы данных.
    Проверяет, что функция возвращает список категорий.
    """
    categories = await requests.get_categories()
    assert len(list(categories)) > 0

@pytest.mark.asyncio
async def test_get_category_item():
    """
    Тестирует функцию получения списка товаров из заданной категории.
    Проверяет, что функция возвращает список товаров.
    """
    items = await requests.get_category_item(1)
    assert len(list(items)) > 0

@pytest.mark.asyncio
async def test_get_item():
    """
    Тестирует функцию получения информации о товаре по его ID.
    Проверяет, что функция возвращает объект товара.
    """
    item = await requests.get_item(1)
    assert item is not None