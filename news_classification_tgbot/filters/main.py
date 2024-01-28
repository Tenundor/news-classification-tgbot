from typing import Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsDigitFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, Any]:
        return message.text.isdigit()
