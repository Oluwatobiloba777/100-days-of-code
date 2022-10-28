from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


YOUR_SMTP_ADDRESS = "YOUR SMTP ADDRESS"
YOUR_MAIL = "YOUR MAIL"
YOUR_PASSWORD = "YOUR PASSWORD"
RECEIVER_EMAIL = "RECEIVER EMAIL"

MY_PRICE = 100

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
"Accept-Language":"en-US,en;q=0.7",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}
response = requests.get(URL,headers=headers)

soup = BeautifulSoup(response.content, "lxml")

# print(soup)

findPrice = soup.find(id="priceblock_ourprice").getText().strip("$")
floatPrice = float(findPrice[1])
# print(findPrice)

title = soup.find(id="productTitle").get_text().strip()
# print(title)


if floatPrice < MY_PRICE:
    message = f"{title} is now {findPrice}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(YOUR_MAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_MAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n{message}\n{URL}"
        )