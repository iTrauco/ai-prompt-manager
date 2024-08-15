import requests
from .config import LLM_API_URL, API_KEY

def send_prompt_to_llm(prompt_content):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(LLM_API_URL, json={"prompt": prompt_content}, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("response", "No response found.")
    else:
        return f"Error: {response.status_code} - {response.text}"
