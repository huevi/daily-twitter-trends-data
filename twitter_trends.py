import pandas as pd
import os

data=pd.DataFrame(data=["1,","2","3"])

consumer_key=os.getenv("consumer_key")
consumer_secret=os.getenv("consumer_secret")
access_token=os.getenv("access_token")
access_token_secret=os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

old_tweet_id = 123


my_fav=api.favorites()

print(my_fav[0])

if not os.path.exists("./data"):
    os.makedirs("./data")

data.to_csv("./data/sample2.csv")