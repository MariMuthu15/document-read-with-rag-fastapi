import os

from langchain_community.vectorstores import FAISS

from src.config import faiss_index_path
from src.services.embeddings import embeddings


def add_documents(docs):
    print("Step 1: Adding documents to FAISS")

    if os.path.exists(
        os.path.join(faiss_index_path, "index.faiss")
    ):
        print("Step 2: Loading existing FAISS index")

        vectorstore = FAISS.load_local(
            faiss_index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )
        print("Step 3: Existing FAISS index loaded")

        vectorstore.add_documents(docs)

    else:
        print("Step 3: Creating new FAISS index")

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
