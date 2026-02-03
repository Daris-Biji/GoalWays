from pydantic_settings import BaseSettings,SettingsConfigDict
from dotenv import load_dotenv
from pydantic import Field



# load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Вместо class Config используем model_config
    # Прописываем  где будут искаться наши файлы
    model_config = SettingsConfigDict(env_file=".env")

    """
    Коротко: Внешний класс — это ЧТО мы хотим получить (данные).
    Внутренний класс — это КАК мы хотим это сделать (правила игры).
    - под капотом работает так что при наследовании "BaseSettings" у нас проверяется атрибут Config
    и если он есть то     то он берет атрибут env_file который говорит где у нас хранятся переменные """

class Settings2(BaseSettings):
    MyPhoneNumber :str =  Field(alias="telephone")

    model_config = SettingsConfigDict(env_file="try.env")


settings = Settings()  # type: ignore[call-arg]

s = Settings2()# type: ignore[call-arg]

print (s.MyPhoneNumber)