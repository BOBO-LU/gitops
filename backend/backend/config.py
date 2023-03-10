from pydantic import BaseSettings


class Settings(BaseSettings):
    # app
    app_name: str = "Awesome API"
    items_per_user: int = 50

    # database
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    # auth
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    # origin
    CLIENT_ORIGIN: str

    class Config:
        env_file = "./.env"


settings = Settings()
