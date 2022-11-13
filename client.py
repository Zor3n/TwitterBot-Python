import tweepy
import os
from dotenv import load_dotenv

load_dotenv()
_consumer_key=os.getenv('CONSUMER_KEY')
_consumer_secret=os.getenv('CONSUMER_SECRET')
_access_token=os.getenv('ACCESS_TOKEN')
_access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
my_bot_id=os.getenv('BOT_ID') #This is the id of this bot account

client = tweepy.Client(
   consumer_key=_consumer_key,
    consumer_secret=_consumer_secret,
    access_token=_access_token,
    access_token_secret=_access_token_secret
)