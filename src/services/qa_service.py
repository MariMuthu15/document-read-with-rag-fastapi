from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

from langchain_classic.chains.retrieval import (
    create_retrieval_chain
)

from langchain_core.prompts import ChatPromptTemplate

from src.config import settings

from src.services.vectorstore import load_vectorstore


llm = ChatGoogleGenerativeAI(
    model=settings.llm_model,
    google_api_key=settings.gemini_key,
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the provided context.

If the answer is not available in the context,
say that you don't have enough information.

<context>
{context}
</context>

Question:
{input}
""")


def get_qa_chain():

    vectorstore = load_vectorstore()

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    qa_chain = create_retrieval_chain(
        vectorstore.as_retriever(
            search_kwargs={
                "k": 4
            }
        ),
        document_chain
    )

    return qa_chain


def ask_question(question: str):

    qa_chain = get_qa_chain()

    response = qa_chain.invoke({
        "input": question
    })

    return response["answer"]
