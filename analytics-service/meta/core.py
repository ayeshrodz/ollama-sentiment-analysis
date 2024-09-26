import requests
import json

def read_file(filepath):
    """Read content from a file."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def analyze_text_with_ollama(model="llama3.2:1b", prompt_file="sentiment_prompt.txt", news_file="news_text.txt", temperature=0.0):
    api_url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json",
    }

    # Read the analysis prompt and the news text from files
    analysis_prompt = read_file(prompt_file)
    news_text = read_file(news_file)
    
    # Combine the prompt with the news text for analysis
    final_prompt = analysis_prompt + "\n\nNews Text: " + news_text
    
    # Prepare the data payload including the configurable temperature
    data = {
        "model": model,
        "prompt": final_prompt,
        "stream": False,
        "options": {
            "temperature": temperature  # Configurable temperature value
        }
    }
    
    try:
        # Send request to the Ollama API
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            return result  # Return the full response including metadata
        else:
            return {"error": f"Failed to analyze text, status code: {response.status_code}, response: {response.text}"}
    
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def generate_analysis_json(news_file, analysis_result, output_file="analysis_output.json"):
    # Read the news text from the file
    news_text = read_file(news_file)
    
    # Create a JSON structure to capture the analysis and full metadata
    result_json = {
        "news_text": news_text,
        "llm_analysis": analysis_result  # Include the response as is
    }
    
    # Write the result to the output file
    with open(output_file, 'w') as outfile:
        json.dump(result_json, outfile, indent=2)
    
    print(f"Analysis result has been written to {output_file}")

# Define the file paths
prompt_file = "sentiment_prompt.txt"
news_file = "news_text.txt"
output_file = "analysis_output.json"

# Configurable temperature (you can set this value dynamically as needed)
temperature_value = 0.7  # Example: you can change this value as needed

# Perform text analysis using Ollama API with the model llama3.2:1b and configurable temperature
analysis_result = analyze_text_with_ollama(model="gemma2:2b", prompt_file=prompt_file, news_file=news_file, temperature=temperature_value)

# Generate and write the analysis JSON output to a file
if analysis_result:
    generate_analysis_json(news_file, analysis_result, output_file=output_file)
