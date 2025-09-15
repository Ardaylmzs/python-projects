import requests
from twilio.rest import Client

OWN_Parameters = "your api link"
key_api = "your api key"
account_sid = 'your sid'
auth_token = 'your token'

weather_params = {
    "lat": 40.946883,
    "lon": 29.163771,
    "appid": key_api,
    "cnt": 4
}

response = requests.get(OWN_Parameters, params=weather_params)
response.raise_for_status()
response_json = response.json()

will_rain = False
for hour_data in response_json["list"]:
    condition_data = hour_data["weather"][0]["id"]
    if int(condition_data) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp: you get number from api server',
        body='opps! RAIN IS COMING SOON , PLEASE TAKE A UMBRELLA 🌧️☔ !!',
        to='whatsapp:your number'
    )
    print(message.sid)
