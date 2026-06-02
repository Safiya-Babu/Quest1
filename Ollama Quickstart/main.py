import requests
def get_response(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result["response"]
prompt = ""
while prompt != "exit":
    prompt = input(">>> ")
    if prompt != "exit":
        res = get_response(prompt)
        print(res)