import smtplib
import pandas as pd
import datetime as dt
import random

# reading files
data = pd.read_csv("Birthday Wisher (Day 32) start/quotes.txt")
data_dict = data.to_dict()

# looking the day
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week==0:
    # random message
    messages = data_dict['MESSAGE']
    random_message = messages[random.randint(0,len(messages))]

    # sending email
    email = "xxxx"
    password = "xxxxxxx"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="xxxxx",
                            msg=f"Subject: Motivational Monday\n\n{random_message}"
        )
