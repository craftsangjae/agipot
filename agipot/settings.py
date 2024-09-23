from pydantic_settings import BaseSettings


class OpenAISettings(BaseSettings):
    openai_api_key: str # OPENAI_API_KEY also works

    class Config:
        env_file = ".env"