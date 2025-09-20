import smtplib
import random
from datetime import datetime
import pandas as pd


MY_EMAIL = "your-email@gmail.com"
MY_PASSWORD ="your-app-password"

today = datetime.now()
today_tuple  = (today.month ,today.day)
try:
    data = pd.read_csv("Ardaylmzs-python-projects/birthday-message/birthdays.csv")
except FileNotFoundError:
    print("Error: 'birthdays.csv' file not found")
    exit()

data_dict ={(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
if today_tuple in data_dict:
    birthday_person = data_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]" , birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg = f"Subject: Happy Birthday!\n\n{letter}")

