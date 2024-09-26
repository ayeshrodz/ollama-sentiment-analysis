import requests
import json
from app.config import Config
import logging

# Initialize logger
logger = logging.getLogger(__name__)

def read_file(filepath):
    """Read content from a file."""
    logger.debug(f"Attempting to read file: {filepath}")
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        logger.debug(f"Successfully read file: {filepath}")
        return content
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise

def analyze_text_with_ollama(model, prompt, news_text, temperature):
    """Send a request to the Ollama API."""
    logger.info(f"Analyzing text with model: {model}, temperature: {temperature}")
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
        logger.debug(f"Ollama API request sent, status code: {response.status_code}")

        if response.status_code == 200:
            logger.info("Ollama API response received successfully.")
            return response.json()  # Return the full response including metadata
        else:
            logger.error(f"Failed to analyze text, status code: {response.status_code}, details: {response.text}")
            return {"error": f"Failed to analyze text, status code: {response.status_code}", "details": response.text}
    except Exception as e:
        logger.exception(f"Error during Ollama API call: {str(e)}")
        return {"error": f"An error occurred: {str(e)}"}
