from decouple import config


class Config:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")


class SourceConfig:
    LANGUAGES_PATH = config("LANGUAGES_PATH")
    DEFAULT_REGION = config("DEFAULT_REGION")
    DEFAULT_URL = config("DEFAULT_URL")
