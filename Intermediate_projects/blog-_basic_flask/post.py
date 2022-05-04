import requests


class Post:
    def __init__(self):
        self.response = ""
        self.data = ""

    def get_data(self):
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.data = self.response.json()
        return self.data
