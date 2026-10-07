from fastapi import APIRouter, UploadFile, File, HTTPException

from src.services.document_service import process_document


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required"
        )

    extension = "." + file.filename.rsplit(".", 1)[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    try:

        print(f"Uploading: {file.filename}")
        print(f"Extension: {extension}")

        result = await process_document(file)

        print(f"Processing result: {result}")

        return {
            "message": "Document uploaded and processed successfully",
            "filename": file.filename,
            "details": result
        }

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Document processing failed: {str(e)}"
        )
    