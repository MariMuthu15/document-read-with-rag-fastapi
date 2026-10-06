from fastapi import APIRouter
from src.models.qa import QuestionRequest, QuestionResponse
from src.services import qa_service


router = APIRouter(
    prefix="/api/qa",
    tags=["Question Answering"]
)


@router.post(
    "/ask",
    response_model=QuestionResponse
)
def ask(request: QuestionRequest):

    answer = qa_service.ask_question(
        request.question
    )

    return QuestionResponse(
        question=request.question,
        answer=answer
    )
