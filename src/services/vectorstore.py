import os

from langchain_community.vectorstores import FAISS

from src.config import faiss_index_path
from src.services.embeddings import embeddings


def add_documents(docs):

    if os.path.exists(
        os.path.join(faiss_index_path, "index.faiss")
    ):

        vectorstore = FAISS.load_local(
            faiss_index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

        vectorstore.add_documents(docs)

    else:

        vectorstore = FAISS.from_documents(
            docs,
            embeddings
        )

    vectorstore.save_local(
        faiss_index_path
    )

    return vectorstore


def load_vectorstore():

    vectorstore = FAISS.load_local(
        faiss_index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore
