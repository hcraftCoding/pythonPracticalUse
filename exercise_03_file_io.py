"""
exercise_03_file_io.py

Simulates saving and loading API response data using file I/O.
Practices open(), context managers, and the json module.

Author: Hunter
Date: 2026-03-21
Tasks:
1.)Write api response dictionary to response.json
    use Python's json module and open with a context manager
2.)Read response.json back
    print the username and tokens remaining in a clean format
3.)Update tokens remaining 
    subtract 100 tokens
    write updated data back to the file
    confirm change by reading and printing again
Analysis:
Step 1:
- open response.json in write mode
- convert api_response dictionary to JSON and save it to the file

Step 2:
- open response.json in read mode
- convert the file contents back to a Python dictionary
- print the username and tokens remaining

Step 3:
- subtract 100 from tokens_remaining
- open response.json in write mode
- write the updated dictionary back to the file
- read and print to confirm
"""

import json

# ── Simulated API response ─────────────────────────────────────────────────────

api_response = {
    "status": "success",
    "user": {
        "id": 1042,
        "username": "hcraft",
        "email": "hcraft.developer@gmail.com",
        "plan": "pro"
    },
    "tokens_remaining": 8500
}

# Write api dictionary to response.json.
with open("response.json", "w") as f: # f is your file, 
    json.dump(api_response, f, indent=2)

# Read json back and print user and tokens remaining
with open("response.json", "r") as f:
    api_response = json.load(f)
    print(f"User: {api_response['user']['username']} | "
          f"Tokens remaining: {api_response['tokens_remaining']}")
    
# Subtract 100 from tokens remaining wrie updated data back to file, read, print again to confirm changes
with open("response.json", "w") as f:
    api_response["tokens_remaining"] -= 100
    json.dump(api_response, f, indent=2)
    
# Confirm 100 subtracted off tokens, read print file
with open("response.json", "r") as f:
    api_response = json.load(f)
    print(f"API response:\n "
          f"status: {api_response['status']}\n"
          f"user:\n"
          f"\t id: {api_response['user']['id']}\n"
          f"\t username: {api_response['user']['username']}\n"
          f"\t email: {api_response['user']['email']}\n"
          f"\t plan: {api_response['user']['plan']}\n"
          f"Tokens remaining: {api_response['tokens_remaining']}")
    
    
                                    