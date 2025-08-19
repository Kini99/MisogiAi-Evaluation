# MisogiAi-Evaluation

## Folder Structure
-- backend/
            main.py -------- API Endpoints


            rag/retriever.py --------- RAG workflow

## Installation

```cd backend
pip install -r requirements.txt```

To check endpoints
```uvicorn backend.main:app --host 0.0.0.0 --port 8000 --log-level info --reload```

- check in swagger docs at http://localhost:8000/docs

To run RAG -
```cd backend
python rag/retreiver.py```