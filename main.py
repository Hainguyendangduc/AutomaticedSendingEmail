import smtplib
import datetime
import pandas as pd
from random import choice

# 2. Check if today matches a birthday in the birthdays.csv
my_email = "hainguyendangduc10122002@gmail.com"
my_password = "ivgmspaamjweenvh"

today = datetime.datetime.now()
month = today.month
day = today.day

data = pd.read_csv("birthdays.csv")
birth_is_today = data[(data['month'] == month) & (data['day'] == day)]
all_letter = ["letter_1.txt", "letter_2.txt", "letter_2.txt"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if data.empty:
    pass
else:
    random_letter = choice(all_letter)
    with open(f"letter_templates/{random_letter}", "r") as file:
        letter = file.read()
    letter = letter.replace("[NAME]", birth_is_today.name.values[0])

email_address = birth_is_today.email.values[0]

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # change GG smtp port
    connection.starttls() # security
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=email_address, msg=letter)

# day 32 - 294. using "python every where" to run this code in the cloud