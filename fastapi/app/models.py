from pydantic import BaseModel, Field
from typing import Optional

class MessageIn(BaseModel):
    content: str = Field(..., min_length=1, description="Content of the message")
    before_id: Optional[str] = Field(None, description="ID of the previous message")

class MessageOut(BaseModel):
    id: str
    content: str
    timestamp: str