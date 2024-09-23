from pydantic_settings import BaseSettings


class OpenAISettings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"