import pandas as pd
import os
import tweepy
import pytz
from datetime import datetime
import time

intz = pytz.timezone('Asia/Kolkata')
nowdt = datetime.now(intz).strftime("%d%m%Y%H%M")
save_filename=f"trends_{nowdt}.csv"



consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

woeid_data=pd.read_csv("./info/india_woeid.txt")

def collect_data(r):
    df = pd.DataFrame.from_dict(api.trends_place(r["woeid"])[0]["trends"])
    df["location"] = r["locality"]
    df["country"] = r["country"]
    df["as_of"] = api.trends_place(r["woeid"])[0]["as_of"]
    df["created_at"] = api.trends_place(r["woeid"])[0]["created_at"]
    return df.copy()

total_trends=pd.DataFrame()
for i,r in woeid_data.iterrows():
    try:
        
        city_trends_df = collect_data(r)
        total_trends=total_trends.append(city_trends_df,ignore_index=True)
        
    except:
        
        time.sleep(300)
        try:
            city_trends_df = collect_data(r)
            total_trends=total_trends.append(city_trends_df,ignore_index=True)
        except:
            print(r["locality"])
            pass
        
if not os.path.exists("./data"):
    os.makedirs("./data")

total_trends.to_csv(f"./data/{save_filename}")