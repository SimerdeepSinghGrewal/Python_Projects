import requests
from twilio.rest import Client

api_key = "2d9264069cd1deb7d96a6aaba5500f2a"
LAT = 51.074600
LON = -113.930412
account_sid = "twillio-account-sid"
auth_token = "twillio-auth-token"
parameters = {
    "lat": 39.362070,
    "lon": -9.157140,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
# print(data['hourly'][0]['weather'][0]['id'])
weather_condition = []
time = []
rain = False
for weather in range(7, 19):
    weather_condition.append(data['hourly'][weather]['weather'][0]['id'])
    if data['hourly'][weather]['weather'][0]['id'] < 700:
        time.append(weather)

        rain = True
if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Its gonna rain at {time}",
        from_="your-twillio number",
        to="your number"
    )

    print(message.status)
