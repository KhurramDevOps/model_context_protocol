import requests

url = "http://localhost:8000/mcp/"

headers = {
    
    "Accept": "text/event-stream, application/json",
}

# Listing all tools
response = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
})

# Calling the tool 'read_doc'
response = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "read_doc",
        "arguments": {"doc_id": "deposition.md"}
    }
})

# Calling the tool 'edit_doc'
response = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "edit_doc",
        "arguments": {"doc_id": "deposition.md", "new_content": "This is a new deposition."}
    }
})

print(response.text)
print("#" * 70)