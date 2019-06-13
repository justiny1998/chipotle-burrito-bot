
from twilio.rest import Client
import tweepy
import re
import time

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1282452336-cMfcPS7Hinj4ZFnVF8VgzwvUDrBwNb9vRXNrKjb'
ACCESS_SECRET = 'H4eagnPS7ODUo79EAAwJSI1vYzuq3eFmNNFVDDBSw17Ev'
CONSUMER_KEY = 'wzyZzobWXCToOvcrTIAMi3xn7'
CONSUMER_SECRET = 'pMYE70fQrcYeOuGwuWawRm5IdNaRSTORL9ZEUWcIIoCtDfSVOJ'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)  

def grab_burrito_code(api):
    statuses = api.user_timeline(id='ChipotleTweets',count=5)
    most_recent_status = statuses[2].text
    status_word_list = most_recent_status.split()
    code = ''
    for i in range(0,len(status_word_list)):
        if status_word_list[i] == '888222':
            if i-2 > 0:
                code = status_word_list[i-2]
    return code

def text_number(code):
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
    
#execution
code = ''
starttime=time.time()
while True:
  code = grab_burrito_code(api)
  print('Trying to find code...')
  if code:
      text_number(code)
      break
  time.sleep(1.0 - ((time.time() - starttime) % 1.0))