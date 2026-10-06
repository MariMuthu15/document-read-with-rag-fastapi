from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import settings

embeddings = GoogleGenerativeAIEmbeddings(
    model=settings.embedding_model,
    google_api_key=settings.gemini_key,
    temperature=0
)