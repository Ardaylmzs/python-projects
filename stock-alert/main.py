import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": os.environ["STOCK_NAME"] ,
    "apikey":os.environ["STOCK_KEY"],
}

response = requests.get(os.environ["STOCK_ENDPOINT"] ,params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_before_data = data_list[1]["4. close"]
yesterday_data = data_list[0]["4. close"]
difference = round(float(yesterday_data) - float(yesterday_before_data))
diff_percentage = (difference/float(yesterday_before_data))*100
up_down = None
if diff_percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if abs(diff_percentage) > 1:
    news_params ={
        "apiKey": os.environ["NEWS_KEY"],
        "qInTitle": os.environ["COMPANY_NAME"],
    }

    news_request = requests.get(os.environ["NEWS_ENDPOINT"] ,params=news_params)
    news_articles = news_request.json()["articles"]
    three_articles = news_articles[:3]
    message_articles = [f"{os.environ["STOCK_NAME"]}: {up_down}{diff_percentage} .\nHeadLines: {article['title']} . \n Brief: {article['description']}" for article in three_articles]
    for article in message_articles:
        client = Client(os.environ["ACCOUNT_SID"], os.environ["AUTH_TOKEN"])
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=article,
            to='whatsapp:+905527268773'
        )
        print(message.sid)



