# Document Read with RAG - FastAPI

A document-based **Retrieval-Augmented Generation (RAG)** API built with **FastAPI, LangChain, Google Gemini, and FAISS**.

Users can upload documents through an API, extract and split the document content, generate embeddings using Gemini, store the embeddings in a FAISS vector database, and ask questions based on the uploaded document content.

## Features

- Upload documents through FastAPI
- PDF document processing
- Automatic document text extraction
- Text chunking using LangChain
- Google Gemini embeddings
- FAISS vector database
- Semantic document retrieval
- Gemini-powered question answering
- REST API with Swagger documentation
- Environment-based configuration
- Built using `uv` for Python dependency management

## Architecture

```text
                    User
                      │
                      │ Upload Document
                      ▼
              ┌───────────────┐
              │    FastAPI    │
              └───────┬───────┘
                      │
                      ▼
              Document Service
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
       Document Loader     File Storage
              │
              ▼
        Text Splitter
              │
              ▼
      Gemini Embeddings
              │
              ▼
          FAISS Index
              │
              │
              │ Ask Question
              ▼
        RAG Retrieval
              │
              ▼
       Relevant Documents
              │
              ▼
       Gemini 2.5 Flash
              │
              ▼
           Answer
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API |
| LangChain | RAG orchestration |
| Google Gemini | Embeddings and LLM |
| FAISS | Vector similarity search |
| PyPDF | PDF document processing |
| Pydantic | Request/response validation |
| uv | Python package and environment management |

## Requirements

Make sure you have:

- Python 3.10+
- `uv`
- Google Gemini API key

### Install uv

If `uv` is not already installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify:

```bash
uv --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/MariMuthu15/document-read-with-rag-fastapi.git
```

Go to the project directory:

```bash
cd document-read-with-rag-fastapi
```

Create the virtual environment:

```bash
uv venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
```

## Environment Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
faiss_index/
data/uploads/
```

## Run the Application

Start FastAPI using:

```bash
uv run uvicorn src.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test all APIs directly from the Swagger interface.

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Upload a Document

### Endpoint

```http
POST /api/documents/upload
```

Upload a PDF document using the `file` form field.

Example using `curl`:

```bash
curl -X POST \
  http://127.0.0.1:8000/api/documents/upload \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@rag_test_document.pdf"
```

Example response:

```json
{
  "message": "Document uploaded and processed successfully",
  "filename": "rag_test_document.pdf",
  "details": {
    "file_id": "8a2d...",
    "chunks": 17,
    "path": "data/uploads/8a2d_rag_test_document.pdf"
  }
}
```

## Ask a Question

### Endpoint

```http
POST /api/qa/ask
```

Request:

```json
{
  "question": "What is Artificial Intelligence?"
}
```

Example response:

```json
{
  "question": "What is Artificial Intelligence?",
  "answer": "Artificial Intelligence is a field of computer science..."
}
```

## RAG Pipeline

The application follows this pipeline:

### 1. Document Upload

The user uploads a document through the FastAPI endpoint.

```text
PDF
 ↓
FastAPI UploadFile
```

### 2. Document Loading

The uploaded PDF is processed using a LangChain document loader.

```text
PDF
 ↓
PyPDFLoader
 ↓
Documents
```

### 3. Text Splitting

Large documents are divided into smaller chunks.

```text
Documents
 ↓
RecursiveCharacterTextSplitter
 ↓
Document Chunks
```

### 4. Embeddings

Each document chunk is converted into a vector using Google Gemini embeddings.

```text
Document Chunk
 ↓
Gemini Embedding
 ↓
Vector
```

### 5. Vector Storage

The vectors are stored in FAISS.

```text
Vectors
 ↓
FAISS
```

### 6. Question Retrieval

When a user asks a question, the question is converted into an embedding and similar document chunks are retrieved.

```text
User Question
 ↓
Embedding
 ↓
FAISS Similarity Search
 ↓
Relevant Chunks
```

### 7. Answer Generation

The retrieved context is provided to Gemini.

```text
Question
   +
Retrieved Context
   ↓
Gemini 2.5 Flash
   ↓
Answer
```

## Testing

A sample test document can be uploaded and queried.

Example questions:

```text
What is Artificial Intelligence?
```

```text
What