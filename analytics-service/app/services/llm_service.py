import requests
import json
from app.config import Config

def read_file(filepath):
    """Read content from a file."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def analyze_text_with_ollama(model, prompt, news_text, temperature):
    """Send a request to the Ollama API."""
    headers = {
        "Content-Type": "application/json",
    }

    # Prepare the data payload including the configurable temperature
    data = {
        "model": model,
        "prompt": f"{prompt}\n\nNews Text: {news_text}",
        "stream": False,
        "options": {
            "temperature": temperature  # Configurable temperature value, allowing 0
        }
    }
    
    try:
        # Send request to the Ollama API
        response = requests.post(Config.OLLAMA_API_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()  # Return the full response including metadata
        else:
            return {"error": f"Failed to analyze text, status code: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
