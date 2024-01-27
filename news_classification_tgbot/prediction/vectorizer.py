import json
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class Vectorizer:
    def __init__(self, vectorizer_data_path: Path):
        with open(str(vectorizer_data_path), "r", encoding="utf-8") as file:
            data_to_load = json.load(file)
        self._vectorizer = TfidfVectorizer(vocabulary=data_to_load["vocabulary_"])
        self._vectorizer.idf_ = np.array(data_to_load["idf_"])

    def transform(self, data: list[str]):
        return self._vectorizer.transform(data)
