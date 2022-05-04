import html_to_json
import requests
import json

response = requests.get("https://time.com/")
json_ = html_to_json.convert(response.text)

print(response.text)
