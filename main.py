
import datetime as dt
import pandas
import random
import smtplib
MY_EMAIL = "melikekurt315@gmail.com"
MY_PASSWORD = "vsvpjbkcvvrqbchi"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month,today_day)


data = pandas.read_csv("Birthday Wisher/birthdays.csv")

birthdays_dict = {(row["month"],row["day"]): row for (index,row) in data.iterrows()}


if today in birthdays_dict:
     birthday_person = birthdays_dict[today]
     with open(f"Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt","r") as letter:
         content = letter.read()
         content = content.replace("[NAME]",birthday_person["name"])


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject: Happy Birthday\n\n{content}")

