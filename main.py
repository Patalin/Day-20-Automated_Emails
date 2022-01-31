# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import smtplib
import datetime as dt
import random
my_password = "your_password"
my_email = "your_email@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email_address_you_want_to_send_the_message",
                            msg=f"Subject:Hello Patalin.py!\n\n{quote}")
