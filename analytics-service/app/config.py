from dotenv import load_dotenv
import os
import logging

# Load environment variables from the .env file
load_dotenv()

class Config:
    # File path for the sentiment prompt
    PROMPT_FILE_PATH = os.getenv('PROMPT_FILE_PATH', 'app/resources/sentiment_prompt.txt')
    
    # Ollama API settings
    OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/generate')

    # Logging configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not provided
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'logs/uvicorn_log.log')

# Set up logging configuration
def setup_logging():
    log_level = getattr(logging, Config.LOG_LEVEL, logging.INFO)
    
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(Config.LOG_FILE_PATH), exist_ok=True)
    
    # Configure the logging module
    logging.basicConfig(
        level=log_level,  # Set log level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
        handlers=[
            logging.FileHandler(Config.LOG_FILE_PATH),  # Write logs to file
            logging.StreamHandler()  # Print logs to console
        ]
    )

# Call the setup_logging function to initialize logging
setup_logging()
