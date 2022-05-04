import pandas
import smtplib
import random, os
import datetime as dt

now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
for date in range(len(data)):
    if now.day == data["day"][date]:
        if now.month == data["month"][date]:
            mail = data["email"][date]
            name = data["name"][date]
            wish_file = random.choice(os.listdir("letter_templates/"))
            with open(f"letter_templates/{wish_file}") as file:
                wish = file.read()
            wish = wish.replace("[NAME]", name)

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login("login email id","password")
                connection.sendmail(
                    from_addr="login email id",
                    to_addrs=mail,
                    msg=f"Subject:Happy Birthday {name}\n\n{wish}"
                )
