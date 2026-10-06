from fastapi import APIRouter, UploadFile, File, HTTPException

from src.services.document_service import process_document


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    try:
        result = await process_document(file)

        return {
            "message": "Document uploaded and processed successfully",
            "filename": file.filename,
            "details": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    