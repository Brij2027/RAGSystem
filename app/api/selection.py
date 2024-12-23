from fastapi import APIRouter
from app.db import SessionLocal

router = APIRouter()

@router.post("/select-documents")
async def select_documents(doc_ids: list[int]):
    async with SessionLocal() as session:
        await session.execute("UPDATE documents SET status=False")
        await session.execute(f"UPDATE documents SET status=True WHERE id IN {tuple(doc_ids)}")
        await session.commit()

    return {"message": "Documents updated successfully"}