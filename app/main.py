from fastapi import FastAPI
from app.api.ingestion import router as ingestion_router
from app.api.qna import router as qna_router
from app.api.selection import router as selection_router
from app.db import init_db

app = FastAPI()

app.include_router(ingestion_router, prefix="/api/v1", tags=["Document Ingestion"])
app.include_router(qna_router, prefix="/api/v1", tags=["Q & A"])
app.include_router(selection_router, prefix="/api/v1", tags=["Document Selection"])


@app.on_event("startup")
async def startup_event():
    try:
        await init_db()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")

if __name__ == "__main__":
    startup_event()