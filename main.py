import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import settings
from news_classification_tgbot import handlers, prediction


async def main():
    predictor = prediction.TextClassificationPredictor(
        vectorizer_data_path=settings.vectorizer_data_path,
        model_data_path=settings.ml_model_data_path,
        target_names_path=settings.target_names_path,
    )
    bot = Bot(token=settings.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, predictor=predictor, ratings=[])


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
