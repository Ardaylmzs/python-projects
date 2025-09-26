import requests
from datetime import datetime

GENDER = input("What gender are you looking for? ")
WEIGHT_KG = int(input("What weight are you looking for? "))
HEIGHT_CM = int(input("What height are you looking for? "))
AGE = int(input("What age are you looking for? "))


APP_ID = "your sheets id"         # you can use sheety, sheety.com
API_KEY = "your sheets api key"

YOUR_USERNAME = "your auth sheets's"   # you can detect the values from sheety
YOUR_PASSWORD = "your sheets password"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "your sheets"                    # you will get endpoint from sheety

exercise_input = input("what did you exercise today ? : ")

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_input,auth=(YOUR_USERNAME, YOUR_PASSWORD))

    print(sheet_response.text)
