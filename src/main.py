from fastapi import FastAPI

from src.routers.document import router as document_router
from src.routers.qa import router as qa_router

app = FastAPI(
    title="Documents Reader App",
    version="1.0.0",
)

app.include_router(document_router)
app.include_router(qa_router)


@app.get("/")
def root():

    return {
        "message": "Document RAG API is running"
    }
