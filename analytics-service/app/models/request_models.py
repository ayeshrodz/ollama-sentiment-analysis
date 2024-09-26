from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class LLMRequest(BaseModel):
    news_title: str
    news_content: str
    temperature_value: float = Field(..., ge=0, lt=1, description="Temperature for LLM response creativity")
    model: str
    news_url: Optional[HttpUrl] = None  # Optional news URL
    published_date: Optional[str] = None  # Optional published date (ISO 8601 format)
