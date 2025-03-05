from pydantic_settings  import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str
    secret_key: str
    algorithm: str
    time_access_token: int

    class Config:
        env_file = ".env"  

settings = Settings()
