import requests
import json
import os

def send_gpt_request(input_message, model, temperature, max_tokens):
    API_KEY = os.environ.get('OPENAI_API_KEY')
    API_ENDPOINT = "https://api.openai.com/v1/chat/completions"


    messages = [
        #{"role": "system", "content": "You are a helpful assistant."}, Can be useful for set the beavior 
        {"role": "user", "content": f"{input_message}"}
    ]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    
    if max_tokens is not None:
        data["max_tokens"] = max_tokens
    
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"[ERROR] Gpt request : {response.status_code}: {response.text}")
    
