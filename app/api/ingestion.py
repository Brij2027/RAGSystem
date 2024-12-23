from typing import List
from fastapi import APIRouter, UploadFile, Form
from app.db import SessionLocal
from app.models.document import Document
from app.core.embeddings import generate_embeddings

router = APIRouter()

async def read_file_with_multiple_encodings(file, encodings: List[str] = None):
    if encodings is None:
        encodings = [
            "utf-8", "utf-16", "latin-1", "iso-8859-1", "windows-1252", "cp1252", "utf-32"
        ]
    
    content = await file.read()
    sanitized_content = content.replace(b'\x00', b'')
    
    for encoding in encodings:
        try:
            return sanitized_content.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Failed to decode the file with any of the following encodings: {', '.join(encodings)}")

@router.post("/ingest")
async def ingest_document(file:UploadFile, description: str = Form(...)):
    content = await read_file_with_multiple_encodings(file)
    embeddings = generate_embeddings(content)


    async with SessionLocal() as session:
        doc = Document(name=file.filename, description=description, content=content)
        doc.set_embeddings(embeddings=embeddings)
        session.add(doc)
        await session.commit()

    return {"message": "Document ingested successfully"}