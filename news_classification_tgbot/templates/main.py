from aiogram.utils.formatting import Bold, Text


def get_welcome_msg(user_full_name: str) -> dict[str]:
    content = Text(
        "Добро пожаловать, ",
        Bold(user_full_name),
        "!\n\n",
        "С помощью бота вы можете определить тематику статьи, на основе ",
        "переданного текста.\n\n",
        "Для взаимодействия с ботом вы можете использовать такие команды:\n\n",
        "/classify_text – анализ текста, переданного в сообщении или файлом. "
        "Принимаются только тексты на английском языке.\n\n",
        "/words_cloud – построение облака слов на основе переданного текста. "
        "Принимаются тексты на английском и русском языках.\n\n",
        "/evaluate – оценка сервиса\n\n",
        "/get_statistics – получение статистики использования бота",
        "/get_rating – получение статистики по рейтингу сервиса",
    )
    return content.as_kwargs()


def get_words_cloud_start_msg() -> dict[str]:
    content = Text(
        "Для построения облака слов передайте текст в сообщении или текстовом " "файле"
    )
    return content.as_kwargs()
