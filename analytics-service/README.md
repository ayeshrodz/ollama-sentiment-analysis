# FastAPI Sentiment Analysis with Ollama LLM

## Overview

This project is a **FastAPI**-based web application designed to perform **sentiment analysis** and other NLP tasks on news articles. The application communicates with an external **Ollama LLM API** to analyze the sentiment of the provided text content, such as news articles. The application is fully configurable through environment variables, features modularized code for scalability, and includes comprehensive logging for error tracking and debugging.

## Key Features

- **Sentiment Analysis**: The application sends news content to the **Ollama LLM API** and retrieves a detailed sentiment analysis report.
- **Modular Structure**: The project is organized into various modules such as routers, services, models, and configuration files for easy scalability and maintenance.
- **Comprehensive Logging**: Logs all key actions, errors, and events to both the console and a log file. The log level can be configured through environment variables.
- **Environment-Based Configuration**: The app uses a `.env` file to configure important variables such as API URLs, log levels, and file paths. This ensures flexibility across different environments like development, staging, and production.
- **API-Based Interaction**: Exposes a REST API where clients can submit news titles and content, and the app will return a detailed analysis based on the LLM's response.

## Installation and Setup

### Prerequisites

Ensure that you have Python 3.7+ installed.

### Clone the Repository

```bash
git clone https://github.com/ayeshrodz/ollama-sentiment-analysis.git
cd ollama-sentiment-analysis
```

### Install Dependencies

You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the root directory with the following environment variables:

   ```bash
   PROMPT_FILE_PATH=app/resources/sentiment_prompt.txt
   OLLAMA_API_URL=http://localhost:11434/api/generate
   LOG_LEVEL=DEBUG
   LOG_FILE_PATH=logs/uvicorn_log.log
   ```

2. You can adjust these variables based on your environment. For example:
   - **`PROMPT_FILE_PATH`**: The file path to the sentiment analysis prompt file.
   - **`OLLAMA_API_URL`**: The URL of the Ollama LLM API.
   - **`LOG_LEVEL`**: Log level can be `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.
   - **`LOG_FILE_PATH`**: Path where the log file will be stored.

### Running the Application

To start the FastAPI application, use the following command:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI application on `http://127.0.0.1:8000`.

### Testing the API

You can test the API by sending a POST request to the `/analyze` endpoint. Here's an example `curl` command:

```bash
curl -X 'POST' 'http://127.0.0.1:8000/analyze'   -H 'Content-Type: application/json'   -d '{
    "news_title": "Economic Downturn in 2023",
    "news_content": "The global economy is expected to shrink by 2.5% this year due to inflation...",
    "temperature_value": 0.3,
    "model": "llama3.2:1b",
    "news_url": "https://news.example.com/economy-downturn",
    "published_date": "2023-09-25"
}'
```

### Logging

The application writes logs to both the console and the log file at the path specified in the `.env` file (`logs/uvicorn_log.log`).

You can control the logging level by setting the `LOG_LEVEL` in the `.env` file to one of the following:

- `DEBUG`: Logs detailed debug information.
- `INFO`: Logs general information and success messages.
- `WARNING`: Logs potential issues.
- `ERROR`: Logs serious issues that need to be addressed.
- `CRITICAL`: Logs very severe error messages.

Example log entry:

```
2023-09-26 11:00:38,846 - app.services.llm_service - INFO - Ollama API response received successfully.
```

### File Structure Explanation

- **`main.py`**: Entry point for the FastAPI application. It includes the routing of the different API endpoints.
- **`config.py`**: Handles application configuration using environment variables. It also sets up logging.
- **`routers/`**: Contains the API route definitions. Each route (e.g., `/analyze`) is modularized into its own file.
- **`services/`**: Contains the core logic for interacting with external services, like calling the Ollama API.
- **`models/`**: Contains the Pydantic models that define the request/response schemas for the API.
- **`resources/`**: Contains static resources like the sentiment prompt text file.
- **`logs/`**: Stores application logs, both for debugging and production error tracking.

### Future Enhancements

- **Database Integration**: Store the results of sentiment analysis for historical tracking and reporting.
- **Authentication**: Add user authentication to the API for secure access.
- **Dockerization**: Package the entire application using Docker for easy deployment.

## Contributing

Feel free to fork this repository and create pull requests. Any improvements, such as adding new features or fixing bugs, are welcome.
