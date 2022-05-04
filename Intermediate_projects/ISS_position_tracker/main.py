import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.074600
MY_LNG = -113.930410


def iss_check():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()
    longitude = float(data1['iss_position']['longitude'])
    latitude = float(data1['iss_position']['latitude'])
    iss_position = (longitude, latitude)
    now = datetime.now()
    if now.hour > 21 and MY_LAT - 5 <= iss_position[1] <= MY_LAT + 5 and MY_LNG - 5 <= iss_position[0] <= MY_LNG + 5:
        condition = True
        print(now.hour)
        print(iss_position)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login("@gmail.com", "password")
            connection.sendmail(
                from_addr="@gmail.com",
                to_addrs="@yahoo.com",
                msg=f"Subject:Watch ISS\n\nISS is moving above you, go outside n have a look"
            )
        while condition:
            time.sleep(60)
            iss_check()
    else:
        condition = False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

iss_check()
