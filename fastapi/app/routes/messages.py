from fastapi import APIRouter, HTTPException
from app.models import MessageIn, MessageOut
from app.database import get_messages, save_message
from app.ws_manager import WSManager
from typing import List
from bson import ObjectId

router = APIRouter()
ws_manager = WSManager()

@router.get("/messages", response_model=List[MessageOut])
def read_messages():
    """Retrieve all messages."""
    return get_messages()

@router.post("/messages", response_model=MessageOut)
def create_message(message: MessageIn):
    """Create a new message."""
    if not message.content.strip():
        raise HTTPException(status_code=400, detail="Message content cannot be empty.")
    if message.before_id and not ObjectId.is_valid(message.before_id):
        raise HTTPException(status_code=400, detail="Invalid before_id format.")
    saved_message = save_message(message.dict())
    return MessageOut(id=str(saved_message.inserted_id), **message.dict())