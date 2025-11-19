from pydantic import BaseModel
from datetime import datetime

# Schema for potential symbols
class SymbolCreate(BaseModel):
    symbol: str
    personal_meaning: str
    category: str

# Schema for creating a dream entry
class DreamCreate(BaseModel):
    content: str
    mood: str
