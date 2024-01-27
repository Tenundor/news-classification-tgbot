import json
from pathlib import Path

from catboost import CatBoostClassifier

from .vectorizer import Vectorizer


class TextClassificationPredictor:
    def __init__(
        self,
        vectorizer_data_path: Path,
        model_data_path: Path,
        target_names_path: Path,
    ):
        self._vectorizer = Vectorizer(vectorizer_data_path)
        self._model = CatBoostClassifier(
            task_type="CPU",
            verbose=False,
            loss_function="MultiClass",
        )
        self._model.load_model(str(model_data_path), format="cbm")
        with open(str(target_names_path), "r", encoding="utf-8") as file:
            self._target_names = json.load(file)

    async def predict(self, data: list[str]):
        data_vec = self._vectorizer.transform(data)
        prediction_index = self._model.predict(data_vec)
        return self._target_names[int(prediction_index)]
