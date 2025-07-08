from pydantic import BaseModel
from typing import Optional

class TweetRequest(BaseModel):
    prompt: str

class Tweet(BaseModel):
    id: Optional[str] = None
    content: str
    status: str  # "draft" or "posted"
