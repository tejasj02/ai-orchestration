import os
import json
import requests

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def lambda_handler(event, context):
    prompt = event.get("prompt", "").strip()
    if not prompt:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Prompt missing"})
        }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        return {
            "statusCode": 200,
            "body": json.dumps({"response": content})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
