from ..prediction import TextClassificationPredictor


async def classify_text(text: str, predictor: TextClassificationPredictor) -> str:
    prediction = await predictor.predict([text])
    return str(prediction)
