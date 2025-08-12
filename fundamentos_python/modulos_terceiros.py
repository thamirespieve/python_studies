import requests

url = "https://www.example.com"

response = requests.get(url)

print(f"Status: {response.status_code}")