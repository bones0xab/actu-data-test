from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    question: str

class Source(BaseModel):
    filename: str
    snippet: str

class QueryResponse(BaseModel):
    answer: Optional[str]
    sources: List[Source]
    no_answer: bool
    reason: Optional[str] = None
