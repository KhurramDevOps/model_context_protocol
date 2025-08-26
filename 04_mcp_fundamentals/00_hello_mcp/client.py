import requests

url = "http://localhost:8000/mcp/"

headers = {
    
    "Accept": "text/event-stream, application/json",
}


response = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
})

print(response.text)
print("#" * 70)