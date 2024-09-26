from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Config:
    # File path for the sentiment prompt
    PROMPT_FILE_PATH = os.getenv('PROMPT_FILE_PATH', 'app/resources/sentiment_prompt.txt')
    
    # Ollama API settings
    OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/generate')

    # Additional configuration variables can be added here
