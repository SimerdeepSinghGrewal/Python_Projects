import requests
from datetime import datetime
import os

APP_ID = "nutritionix api id"
API_KEY = "nutritionix api key"

GENDER = "male"
WEIGHT = "75"
HEIGHT = "170"
AGE = "30"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercise you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(endpoint, json=parameters, headers=headers)
data = response.json()
print(data)
today = datetime.now()
header = {"Authorization": "sheety auth code"}
sheet_endpoint = "https://api.sheety.co/6aa9dd41f29635f066aa6f698e12fc94/workoutTracking/workouts"
nutri_data = {
    "workout": {
        "exercise": data["exercises"][0]["name"].title(),
    }
}
sheet_add = requests.put("https://api.sheety.co/6aa9dd41f29635f066aa6f698e12fc94/workoutTracking/workouts/3",
                         json=nutri_data, headers=header)
print(sheet_add.text)
