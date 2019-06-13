
from twilio.rest import Client
import tweepy
import re

cache = []

def grab_burrito_code(api):
    #grab most recent status
    statuses = api.user_timeline(id='ChipotleTweets',count=5)
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
    account_sid = 'ACCOUNT_SID_HERE'
    auth_token = 'ACCOUNT_TOKEN_HERE'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=code,
                     from_='+TWILIO_PHONE_NUMBER_HERE',
                     to='+888222'
                 )
    print("Message sent to Chipotle!")
    
