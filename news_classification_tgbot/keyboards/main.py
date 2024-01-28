from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_evaluating_keyboard():
    kb = [[KeyboardButton(text=str(rating)) for rating in range(1, 6)]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
