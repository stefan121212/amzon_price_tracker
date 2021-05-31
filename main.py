import smtplib
import requests
import lxml
from bs4 import BeautifulSoup
from smtplib import SMTP

EMAIL = "Target_email"
PASSWORD = "password of email"

url = "https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "sr-RS,sr;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,fr;q=0.5,hr;q=0.4,tr;q=0.3,bs;q=0.2"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-size-base a-color-price").getText()
price_without_dollar = price.split("$")[1]
price_float = float(price_without_dollar)
print(price_float)

if price_float < 400:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Price of console is {price_float}$"
                            )