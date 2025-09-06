import smtplib
import random
from datetime import datetime
import pandas
MY_EMAIL = "ardaylmz1163@gmail.com"
MY_PASSWORD = "dmrtytwztsofqftg"

today = datetime.now()
today_tuple  = (today.month ,today.day)
data = pandas.read_csv("birthdays.csv")
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
        connection.sendmail(MY_EMAIL, birthday_person["email"], f"BIRTHDAY MESSAGE\n\n{letter}")

