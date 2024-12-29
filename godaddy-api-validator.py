import os
import requests

# Retrieve the API key from an environment variable
api_key = os.getenv('GODADDY_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the GODADDY_API_KEY environment variable.")

# Use the API key to make a request
url = "https://api.godaddy.com/v1/domains"
headers = {
    "Authorization": f"sso-key {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API request successful")
else:
    print(f"API request failed with status code {response.status_code}")
