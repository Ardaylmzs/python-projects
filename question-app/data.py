import requests

parameters = {
        "amount": 10,
        "type": "boolean"
}
response = requests.get("quiz-resources API" , params=parameters)
response.raise_for_status()
data = response.json()
question_data= data["results"]

