import yagmail
import os
import pandas as pd
import time
from dotenv import load_dotenv
from news import NewsFeed
from datetime import date
from datetime import timedelta
from datetime import datetime


load_dotenv()

GMAIL = os.getenv('GMAIL')
PWD = os.getenv('PWD')

today = date.today()
yesterday = today - timedelta(days=1)

recipient = pd.read_excel('people.xlsx')


def send_email():
    email = yagmail.SMTP(user=GMAIL, password=PWD)
    for index, row in recipient.iterrows():
        news_feed = NewsFeed(row['interest'], yesterday, today)
        email.send(to=row['email'],
                   subject=f"Your {row['interest']} News Feed for today!",
                   contents=f"Dear {row['name']},\n\n{news_feed.get()}\n\nBest regards,\nBennis Yiu")
        print('email for ' + row['name'] + ' ' +
              row['surname'] + ' has been sent!')


send_email()
print('All emails have been sent!')
