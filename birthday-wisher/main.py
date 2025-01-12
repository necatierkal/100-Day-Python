#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.



from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "necatierkal67@gmail.com"
MY_PASSWORD = "rejpfpfruzzbgyvt"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

























####For Remember How to Use
#


# import smtplib
#
# my_email = "necatierkal67@gmail.com"
# password = "rejpfpfruzzbgyvt"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ne.erkal22@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my mail.")
# import datetime as dt
# import random
# import smtplib
#
# my_email = "necatierkal67@gmail.com"
# password = "rejpfpfruzzbgyvt"
#
#
# now = dt.datetime.now()
# # year=now.year
# # month = now.month
# day_of_week = now.weekday()
# #
# # print(now)
#
# date_of_birth = dt.datetime(year=1988,month=7,day=21)
# # print(date_of_birth)
#
# if day_of_week == 0:
#     with open("quotes.txt","r") as quote:
#         quote_list = quote.readlines()
#         quote_to_send = random.choice(quote_list)
#
#         with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=my_email,
#                 msg=f"Subject:Monday Motivation\n\n{quote_to_send}")