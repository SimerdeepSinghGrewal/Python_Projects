import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "api-token"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Pushup Graph",
    "unit": "repetition",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1008",
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
update_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_pixel_config = {
    "quantity": "1050"
}

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)