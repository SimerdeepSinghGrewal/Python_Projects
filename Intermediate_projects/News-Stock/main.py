import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_key = "newsapi.org--api-key"
account_sid = "your-twillio-account-sid"
auth_token = "your-twillio-auth-token"


def percentage(yester, day_b_yes):
    diff = yester - day_b_yes
    percen = (diff / yester) * 100
    return round(percen, 2)



now = datetime.datetime.now()
weekday = now.weekday()
today_day = now.day
today_mon = now.month
today_yr = now.year
STOCK_API_key = "AWKQ74LQLGUYLP2I"
parameter = {
    "function": "TIME_SERIES_INTRADAY", # DAILY-->used by default
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "full",
    "apikey": STOCK_API_key
}
response = requests.get("https://www.alphavantage.co/query", params=parameter)
response.raise_for_status()
data = response.json()
# print(data["Time Series (60min)"]['2022-03-25 20:00:00']["4. close"])
if weekday == 0:
    yesterday = today_day - 3
    day_bef_yes = today_day - 4
elif weekday == 1:
    yesterday = today_day - 1
    day_bef_yes = today_day - 4
elif weekday == 6:
    yesterday = today_day - 2
    day_bef_yes = today_day - 3
else:
    yesterday = today_day - 1
    day_bef_yes = today_day - 2

one_bef = float(data["Time Series (60min)"][f"2022-03-{yesterday} 20:00:00"]["4. close"])
two_bef = float(data["Time Series (60min)"][f"2022-03-{day_bef_yes} 20:00:00"]["4. close"])
print(one_bef)
print(two_bef)
perc = percentage(one_bef, two_bef)
print(perc)
param = {
    "q": COMPANY_NAME,
    "from": f"{today_yr}-{today_mon}-{day_bef_yes}",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": NEWS_API_key,
}
if perc >= 5 or perc <= -5:
    response = requests.get("https://newsapi.org/v2/everything", params=param)
    data = response.json()
    for news in range(0, 3):
        # print(f"{data['articles'][news]['title']}\n{data['articles'][0]['description']}\n\n")
        client = Client(account_sid, auth_token)
        if perc >= 5:
            message = client.messages.create(
                body=f"TSLA 🔺{perc}%\nHeadline:{data['articles'][news]['title']}\nBrief:{data['articles'][news]['description']}",
                from_="twillio-number",
                to="your-number"
            )
            print(message.status)
        elif perc <= -5:
            message = client.messages.create(
                body=f"TSLA 🔻{perc}%\nHeadline:{data['articles'][news]['title']}\nBrief:{data['articles'][news]['description']}",
                from_="twillio-number",
                to="your-number"
            )
            print(message.status)
