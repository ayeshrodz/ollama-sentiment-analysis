from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
import requests
import json
from typing import Optional

# Initialize FastAPI app
app = FastAPI()

# Define the request body using Pydantic
class LLMRequest(BaseModel):
    news_title: str
    news_content: str
    temperature_value: float = Field(..., ge=0, lt=1, description="Temperature for LLM response creativity")
    model: str
    news_url: Optional[HttpUrl] = None  # Optional news URL
    published_date: Optional[str] = None  # Optional published date (ISO 8601 format)

# Function to read the prompt from the file
def read_file(filepath):
    """Read content from a file."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content

# Function to send the request to the LLM (Ollama API)
def analyze_text_with_ollama(model, prompt, news_text, temperature):
    api_url = "http://localhost:11434/api/generate"  # Example of Ollama's API
    headers = {
        "Content-Type": "application/json",
    }

    # Prepare the data payload including the configurable temperature
    data = {
        "model": model,
        "prompt": f"{prompt}\n\nNews Text: {news_text}",
        "stream": False,
        "options": {
            "temperature": temperature  # Configurable temperature value
        }
    }
    
    try:
        # Send request to the Ollama API
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()  # Return the full response including metadata
        else:
            return {"error": f"Failed to analyze text, status code: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# The FastAPI POST endpoint
@app.post("/analyze")
def analyze_news(request: LLMRequest):
    # Read the predefined prompt (assuming it's stored in a text file)
    prompt_file = "sentiment_prompt.txt"  # File path to the prompt
    prompt = read_file(prompt_file)

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
