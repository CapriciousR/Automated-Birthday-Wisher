##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Constants
EMAIL = "test@gmail.com"
PASSWORD = "testpass"

import datetime as dt
import pandas
from random import randint
import smtplib

now = dt.datetime.now()
curr_year = now.year
curr_month = now.month
curr_day = now.day

bdays = pandas.read_csv("birthdays.csv")

# Send email function

def sendEmail(name, email):
    num = randint(1,3)
    with open(f"letter_templates/letter_{num}.txt","r") as letter_file:
        letter_base = letter_file.read()
        letter = letter_base.replace('[NAME]',name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, 
                                to_addrs=email, 
                                msg=f"Subject:Happy Birthday\n\n{letter}"
                                )

for index,row in bdays.iterrows():
    if (curr_month == row['month'] and curr_day == row['day']):
        sendEmail(name=row['name'],email=row['email'])
        print(f"Mail successfully sent to {row['name']}")
