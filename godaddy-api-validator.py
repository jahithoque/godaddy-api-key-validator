import os
import requests
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Script to interact with GoDaddy APIs")
parser.add_argument('--godaddy_api_key', required=True, help='GoDaddy API Key')


# Parse the arguments
args = parser.parse_args()

godaddy_api_key = args.godaddy_api_key

# Function to interact with GoDaddy API
def godaddy_api_request(endpoint, data=None):
    url = f"https://api.godaddy.com/v1/{endpoint}"
    headers = {
        "Authorization": f"sso-key {godaddy_api_key}",
        "Content-Type": "application/json"
    }

    if data:
        response = requests.post(url, headers=headers, json=data)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("GoDaddy API request successful")
        return response.json()
    else:
        print(f"GoDaddy API request failed with status code {response.status_code}")
        return None

# Example usage
godaddy_response = godaddy_api_request("domains")
if godaddy_response:
    print(godaddy_response)
