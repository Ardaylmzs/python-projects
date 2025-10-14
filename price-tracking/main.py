import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

practice_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url=practice_url,headers=header).content
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
price = soup.find(class_="a-offscreen").get_text()
print(price)

price_without_currency = price.split("$")[1]
print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < 12:
    msg = "BE FAST!! there are a opportunity in your preferences , DON'T miss that!!"
    with smtplib.SMTP(os.environ["SMTP_MAİL"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_MAİL"],password=os.environ["MY_PASSWORD"])
        connection.sendmail(from_addr=os.environ["MY_MAİL"],
                            to_addrs=os.environ["TO_MAİL"],
                            msg=f"subject: PRICE ALERT.\n\nBE FAST!! there are a opportunity in your preferences ,"
                                f" DON'T miss that!! Price is only ${price} :) ".encode("utf-8"))





