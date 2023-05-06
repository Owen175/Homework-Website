from pydantic import BaseSettings

class Config(BaseSettings):
    sqlAlchemyLink: str

    class Config:
        env_file = '.env'


config = Config()