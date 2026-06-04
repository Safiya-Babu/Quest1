import requests
import json

def get_response(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": True
    }

    response = requests.post(url, json=data, stream=True)

    for line in response.iter_lines():
        if line:
            result = json.loads(line)
            print(result["response"], end="")

prompt = ""

while prompt != "exit":
    prompt = input(">>> ")

    if prompt != "exit":
        get_response(prompt)