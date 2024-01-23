from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from .. import templates


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        templates.welcome_msg,
    )