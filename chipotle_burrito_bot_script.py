
from twilio.rest import Client
import tweepy
import re

cache = []

def grab_burrito_code(api):
    #grab most recent status
    statuses = api.user_timeline(id='JustinY1998',count=5)
    most_recent_status = statuses[0].text

    #if we have already encountered this tweet do nothing
    if cache.count(most_recent_status) > 0:
        return ''
    
    status_word_list = most_recent_status.split()
    code = ''
    #grab code
    for i in range(0,len(status_word_list)):
        if status_word_list[i] == '888222':
            if i-2 >= 0:
                code = status_word_list[i-2]

    cache.append(most_recent_status)
    return code

def text_to_number(code):
    account_sid = 'AC9b701d6b1f21883b1fecf80871887afe'
    auth_token = '57225797a6524c537baf51613eda4582'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=code,
                     from_='+16504762859',
                     to='+888222'
                 )
    print("Message sent to Chipotle!")
    