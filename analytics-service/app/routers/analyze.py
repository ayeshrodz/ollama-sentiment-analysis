from fastapi import APIRouter
from app.models.request_models import LLMRequest
from app.services.llm_service import analyze_text_with_ollama, read_file
from app.config import Config

# Define the router
router = APIRouter()

# Define the POST endpoint
@router.post("/analyze")
def analyze_news(request: LLMRequest):
    # Read the predefined prompt (assuming it's stored in a text file)
    prompt = read_file(Config.PROMPT_FILE_PATH)

    # Make a call to the Ollama API with the parameters
    result = analyze_text_with_ollama(
        model=request.model, 
        prompt=prompt,
        news_text=f"{request.news_title}\n{request.news_content}",
        temperature=request.temperature_value
    )
    
    # Return the full analysis result along with optional parameters
    return {
        "news_title": request.news_title,
        "news_content": request.news_content,
        "news_url": request.news_url,
        "published_date": request.published_date,
        "llm_analysis": result
    }
