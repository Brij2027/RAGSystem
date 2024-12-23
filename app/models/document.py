from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
import json

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    content = Column(String, nullable=False)
    embeddings = Column(JSONB, nullable=True)
    status = Column(Boolean, default=True)

    def set_embeddings(self, embeddings):
        """Serialize embeddings into JSON before storing them in the database."""
        self.embeddings = json.dumps(embeddings)

    def get_embeddings(self):
        """Deserialize embeddings from JSON stored in the database."""
        return json.loads(self.embeddings) if self.embeddings else None
