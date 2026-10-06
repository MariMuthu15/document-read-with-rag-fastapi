from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Documents Reader App"
    database_url: str = ""
    gemini_key: str = ""
    embedding_model: str = "models/gemini-embedding-2"
    llm_model: str = "gemini-2.5-flash"
    faiss_index_path: str = "./faiss_index"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

faiss_index_path = settings.faiss_index_path