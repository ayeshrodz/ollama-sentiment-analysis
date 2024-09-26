from fastapi import APIRouter
from app.models.request_models import LLMRequest
from app.services.llm_service import analyze_text_with_ollama, read_file
from app.config import Config
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Define the router
router = APIRouter()

# Define the POST endpoint
@router.post("/analyze")
def analyze_news(request: LLMRequest):
    logger.info(f"Received request to analyze news: {request.news_title}")
    
    try:
        # Read the predefined prompt (assuming it's stored in a text file)
        prompt = read_file(Config.PROMPT_FILE_PATH)

        # Make a call to the Ollama API with the parameters
        result = analyze_text_with_ollama(
            model=request.model, 
            prompt=prompt,
            news_text=f"{request.news_title}\n{request.news_content}",
            temperature=request.temperature_value
        )
        
        logger.info(f"Analysis completed for: {request.news_title}")
        # Return the full analysis result along with optional parameters
        return {
            "news_title": request.news_title,
            "news_content": request.news_content,
            "news_url": request.news_url,
            "published_date": request.published_date,
            "llm_analysis": result
        }
    except Exception as e:
        logger.exception("Error occurred during analysis")
        return {"error": f"An error occurred: {str(e)}"}
