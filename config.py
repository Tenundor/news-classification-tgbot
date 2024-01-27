from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr

    vectorizer_data_path: Path = Path("data/vectorizer_data.json")
    ml_model_data_path: Path = Path("data/catboost_model.cbm")
    target_names_path: Path = Path("data/target_names.json")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
