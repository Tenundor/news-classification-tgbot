from aiogram.utils.formatting import Bold, Text


def get_welcome_msg(user_full_name: str) -> dict[str]:
    content = Text(
        "Добро пожаловать, ",
        Bold(user_full_name),
        "!\n",
        "С помощью бота вы можете определить тематику статьи на основе ",
        "переданного текста.\n\n",
        "Для взаимодействия с ботом вы можете использовать команды:\n\n",
        "/classify_text – анализ текста, переданного в сообщении. "
        "Принимаются только тексты на английском языке.\n",
        "/words_cloud – построение облака слов на основе переданного текста. "
        "Принимаются тексты на английском и русском языках.\n",
        "/evaluate – оценка сервиса\n",
        "/get_rating – получение статистики по рейтингу сервиса",
    )
    return content.as_kwargs()


def get_words_cloud_start_msg() -> dict[str]:
    content = Text(
        "Для построения облака слов передайте текст в сообщении на английском или "
        "русском языках"
    )
    return content.as_kwargs()


def get_text_classify_msg() -> dict[str]:
    content = Text(
        "Для классификации тематики передайте текст в сообщении на английском языке"
    )
    return content.as_kwargs()


def get_prediction_out_msg(text_classification: str) -> dict[str]:
    content = Text(f"Предположительная тематика текста: {text_classification}")
    return content.as_kwargs()


def get_bot_evaluating_msg() -> dict[str]:
    content = Text("Оцените бота по шкале от 1 до 5")
    return content.as_kwargs()


def get_thanks_for_rating_msg() -> dict[str]:
    content = Text("Спасибо за вашу оценку!")
    return content.as_kwargs()


def get_invalid_rating_msg() -> dict[str]:
    content = Text("Выберите оценку от 1 до 5.")
    return content.as_kwargs()


def get_inability_to_process_msg() -> dict[str]:
    content = Text(
        "К сожалению, мы не можем обработать ваше сообщение. Используйте "
        "одну из доступных команд бота"
    )
    return content.as_kwargs()


def get_no_ratings_msg() -> dict[str]:
    content = Text("Бот пока не получил ни одной оценки")
    return content.as_kwargs()


def get_avg_rating_msg(avg_rating: float) -> dict[str]:
    content = Text(f"Средняя оценка бота: {avg_rating}")
    return content.as_kwargs()
