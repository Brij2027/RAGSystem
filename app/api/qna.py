from sqlalchemy.future import select
from typing import List
from fastapi import APIRouter, HTTPException
from app.db import SessionLocal
from app.models.document import Document
from app.core.embeddings import generate_embeddings
from app.core.retriever import retrieve_similar
from app.core.answer_generator import generate_answer_from_context


router = APIRouter()

@router.post("/qna")
async def get_answer(question:  str):
    query_embedding = generate_embeddings(question)

    async with SessionLocal() as session:
        result = await session.execute(
            select(Document).filter(Document.status == True)
        )

        documents = result.scalars().all()

        document_embeddings = [(doc.id, doc.get_embeddings()) for doc in documents]

        similar_docs = retrieve_similar(query_embedding, document_embeddings)
        similar_doc_ids = [doc_id for doc_id, _ in similar_docs]
        print([doc.id for doc in documents], similar_doc_ids)
        relevant_documents = [doc for doc in documents if doc.id in similar_doc_ids]
        
        if not relevant_documents:
            raise HTTPException(status_code=404, detail="No relevant documents found.")
        
        # Step 5: Generate an answer based on the retrieved documents
        context = "\n".join([doc.content for doc in relevant_documents])
        answer = generate_answer_from_context(question, context)
        
        return {"answer": answer, "relevant_documents": similar_docs}

        return {"similar_documents": similar_docs}