from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from .. import filters, keyboards, services, templates
from ..prediction import TextClassificationPredictor
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


@router.message(Command("classify_text"))
async def cmd_classify_text(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(States.text_classification_state)
    await message.answer(
        **templates.get_text_classify_msg(),
    )


@router.message(States.text_classification_state)
async def process_text_classification(
    message: Message, state: FSMContext, predictor: TextClassificationPredictor
):
    text = message.text
    prediction = await services.classify_text(text, predictor)
    await message.answer(**templates.get_prediction_out_msg(prediction))
    await state.clear()


@router.message(Command("evaluate"))
async def cmd_evaluate_bot(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        **templates.get_bot_evaluating_msg(),
        reply_markup=keyboards.get_evaluating_keyboard(),
    )
    await state.set_state(States.bot_evaluating_state)


@router.message(F.text, filters.IsDigitFilter(), States.bot_evaluating_state)
async def process_rating(message: Message, state: FSMContext, ratings: list[int]):
    rating = int(message.text)
    if 1 <= rating <= 5:
        ratings.append(rating)
        await message.answer(
            **templates.get_thanks_for_rating_msg(),
            reply_markup=ReplyKeyboardRemove(),
        )
        await state.clear()
    else:
        await message.answer(**templates.get_invalid_rating_msg())


@router.message(Command("get_rating"))
async def cms_get_rating(message: Message, state: FSMContext, ratings: list[int]):
    await state.clear()
    if len(ratings) == 0:
        await message.answer(**templates.get_no_ratings_msg())
    else:
        avg_rating = round(sum(ratings) / len(ratings), 0)
        await message.answer(**templates.get_avg_rating_msg(avg_rating))


@router.message()
async def process_unknown_message(message: Message):
    await message.reply(**templates.get_inability_to_process_msg())
