import chipotle_burrito_bot_script as chipotle
import time
import tweepy
import re

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'ACCESS_TOKEN_HERE'
ACCESS_SECRET = 'ACCESS_SECRET_HERE'
CONSUMER_KEY = 'CONSUMER_KEY_HERE'
CONSUMER_SECRET = 'CONSUMER_SECRET_HERE'

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
