from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    words_cloud_state = State()
    text_classification_state = State()
    bot_evaluating_state = State()
