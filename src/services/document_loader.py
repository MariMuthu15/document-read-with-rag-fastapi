from pathlib import Path
from src.config import settings

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(file_path: str):

    extension = Path(file_path).suffix.lower()
    print(f"Loading document: {file_path}")

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".docx":
        print(f"Loading DOCX document: {file_path}")
        loader = Docx2txtLoader(file_path)

    elif extension == ".txt":
        print(f"Loading TXT document: {file_path}")
        loader = TextLoader(
            file_path,
            encoding="utf-8"
        )

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )

    return splitter.split_documents(documents)