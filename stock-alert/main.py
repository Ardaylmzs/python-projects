import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "your api key"
NEWS_KEY = "your api key"


account_sid = "your account sid"
auth_token = "your auth token"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

response = requests.get(STOCK_ENDPOINT ,params=stock_params)
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
        "apiKey": NEWS_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_request = requests.get(NEWS_ENDPOINT ,params=news_params)
    news_articles = news_request.json()["articles"]
    three_articles = news_articles[:3]
    message_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage} .\nHeadLines: {article['title']} . \n Brief: {article['description']}" for article in three_articles]
    for article in message_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:twilio whatsapp number',
            body=article,
            to='whatsapp:your whatsapp'
        )
        print(message.sid)



