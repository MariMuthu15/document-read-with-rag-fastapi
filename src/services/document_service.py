import os
import uuid

from fastapi import UploadFile

from src.services.document_loader import load_document
from src.services.vectorstore import add_documents


UPLOAD_DIR = "data/uploads"


async def process_document(file: UploadFile):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}_{file.filename}"
    )

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    docs = load_document(file_path)

    print("STEP 4: Document loaded")
    print("Number of documents:", len(docs))

    print("STEP 5: Adding documents to FAISS")

    add_documents(docs)

    print("STEP 6: Added documents to FAISS")

    return {
        "file_id": file_id,
        "chunks": len(docs),
        "path": file_path
    }