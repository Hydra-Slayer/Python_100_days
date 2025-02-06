import smtplib
import datetime
import pandas

dates_data = pandas.read_csv("birthdays.csv")
# print(dates_data)
b =str(datetime.datetime.now())

dates_dict = dates_data.to_dict(orient='records')
# print(dates_dict[0]['month'])
current_date  = b.split(" ")[0].split("-")
current_day = current_date[2]
current_month = current_date[1]
# print(current_month)
# print(int(current_day) == 4)
MY_EMAIL = test@gmail.com
MY_PWD = "123456"
for item in dates_dict:
    if item["month"] ==int(current_month):
        if item["day"] ==int(current_day):
            with open("letter") as letter_file:
               contents = letter_file.read()
               contents = contents.replace("[NAME]",item["name"])
            with smtplib.SMTP("smtp.gmil.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL,MY_PWD)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=item["email"],
                    msg=f"Subject: Happy Birthday!\n\n{contents}"
                )
