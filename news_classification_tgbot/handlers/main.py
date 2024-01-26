from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from .. import services, templates
from ..states import States


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        **templates.get_welcome_msg(message.from_user.full_name),
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("words_cloud"))
async def cmd_words_cloud(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(States.words_cloud_state)
    await message.answer(
        **templates.get_words_cloud_start_msg(),
    )


@router.message(States.words_cloud_state)
async def process_words_cloud(message: Message, state: FSMContext):
    text = message.text
    word_cloud_image = await services.create_word_cloud(text)
    await message.answer_photo(word_cloud_image)
    await state.clear()
