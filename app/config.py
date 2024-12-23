import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgres+asyncpg://admin:root@db:5432/document_db")
    EMBEDDING_DIM = 768