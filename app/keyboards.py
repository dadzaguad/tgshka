from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Корзина")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="О нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="выберите пункт меню",
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="футболки", callback_data="t-shirts")],
        [InlineKeyboardButton(text="шорты", callback_data="shorts")],
        [InlineKeyboardButton(text="кепки", callback_data="hats")],
    ]
)

get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Отправить номер телефона", request_contact=True)]],
    resize_keyboard=True,
    input_field_placeholder="введите номер телефона",
)
