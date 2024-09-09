import pandas as pd
import smtplib
import datetime as dt
import random

PLACEHOLDER = "[NAME]"

# Reading CSV file
data = pd.read_csv("birthdays.csv")

# Get the current date
today = dt.datetime.now()

my_email = 'riteshbill14@gmail.com'
password = 'abc123()'

'''Extracting the year, month and date.
print(today.year)
print(today.month)
print(today.day)
'''

# looping through pandas
for label, row in data.iterrows():
    num = random.randint(1, 3)

    # Reading the content from the file
    with open(f'letter_templates/letter_{num}.txt') as file:
        message = file.read()

    if today.month == row['month'] and today.day == row['day']:
        birthday_msg = message.replace(PLACEHOLDER, row['name'])

        # Sending mails to the birthday person
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user= my_email,password= password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= row['email'],
                msg="Subject:Birthday Wish"
                    f"\n \n {birthday_msg}"
            )


