from io import BytesIO

import nltk
from aiogram.types import BufferedInputFile
from nltk.corpus import stopwords
from wordcloud import WordCloud


nltk.download("stopwords")


stopwords_set = set(stopwords.words("russian")) | set(stopwords.words("english"))


async def create_word_cloud(text: str) -> BufferedInputFile:
    word_cloud = WordCloud(
        width=1600,
        height=1200,
        stopwords=stopwords_set,
    ).generate(text)
    image = word_cloud.to_image()

    with BytesIO() as output:
        image.save(output, format="PNG")
        output.seek(0)
        return BufferedInputFile(output.read(), filename="word_count.png")
