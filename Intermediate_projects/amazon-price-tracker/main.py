import lxml
from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.ca/Echo-Dot-3rd-gen-Charcoal/dp/B07PDHT5XP/ref=sr_1_3?crid=20X0XQEO9ZM6U&keywords=alexa&qid" \
      "=1649204652&sprefix=alexa%2Caps%2C155&sr=8-3 "

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}
response = requests.get(URL, headers=header)
data = response.text

soup = BeautifulSoup(data, "lxml")
product_name = soup.find(name="span", id="productTitle").get_text()
price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])

if price <= 24.99:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("login email id", "password")
        connection.sendmail(
            from_addr="login email id",
            to_addrs="where to send",
            msg=f"Subjec: Price Drop Alert for {product_name}\n\n The price has dropped to your expectation\n{URL}"
        )