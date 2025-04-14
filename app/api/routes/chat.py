"""
Chat routes for ChatXpert
© 2024-2025 ELYES. All rights reserved.
Done by ELYES
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from app.core.database import mongodb, redis_client
from app.core.security import get_current_user

# Done by ELYES
router = APIRouter()

class ChatMessage(BaseModel):
    # Done by ELYES
    content: str
    timestamp: datetime = datetime.now()
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    # Done by ELYES
    message: str
    confidence: float
    intent: Optional[str] = None

@router.post("/send", response_model=ChatResponse)
async def send_message(
    message: ChatMessage,
    current_user = Depends(get_current_user)
):
    # Done by ELYES
    try:
        # Store message in MongoDB
        await mongodb.messages.insert_one({
            "content": message.content,
            "user_id": current_user.id,
            "timestamp": message.timestamp
        })
        
        # TODO: Implement AI processing logic here
        # For now, return a simple response
        return ChatResponse(
            message="I received your message. AI processing will be implemented soon.",
            confidence=1.0,
            intent="general"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[ChatMessage])
async def get_chat_history(
    limit: int = 50,
    current_user = Depends(get_current_user)
):
    # Done by ELYES
    try:
        cursor = mongodb.messages.find(
            {"user_id": current_user.id}
        ).sort("timestamp", -1).limit(limit)
        
        messages = await cursor.to_list(length=limit)
        return [ChatMessage(**msg) for msg in messages]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 