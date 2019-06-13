import chipotle_burrito_bot_script as chipotle
import time
import tweepy
import re

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

code = ''
starttime=time.time()

while True:
  code = chipotle.grab_burrito_code(api) 
  print('Trying to find code...')
  if code:
      chipotle.text_to_number(code)
  time.sleep(1.0 - ((time.time() - starttime) % 1.0))