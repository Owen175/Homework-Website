from pydantic import BaseSettings

class Settings(BaseSettings):
    sqlAlchemyLink: str

    class Config:
        env_file = '.env'


config = Settings()
