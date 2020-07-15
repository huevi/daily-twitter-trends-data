import pandas as pd
import os
import tweepy

data=pd.DataFrame(data=["1,","2","3"])

consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")

# print(consumer_key)
print(type(consumer_key))
print(type(consumer_secret))
print(type(access_token))
print(type(access_token_secret))

# print((consumer_key))
# print((consumer_secret))
# print((access_token))
# print((access_token_secret))
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# old_tweet_id = 123


my_fav=api.favorites()

print(my_fav[0])

if not os.path.exists("./data"):
    os.makedirs("./data")

data.to_csv("./data/sample2.csv")