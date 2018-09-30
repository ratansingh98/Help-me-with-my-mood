# Neccessary Libraries
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from textblob import TextBlob
from datetime import datetime, date, time, timedelta
import re
import os
import pandas as pd
import numpy as np

# Perform Authentication


def authenticate():
    consumer_key = 'uxVdIpEHiOC5V8emdcqQefWu3'
    consumer_secret = 'EsKr2toFjckmXzfdbwpcUl4n0EHT1gcXJfBg5DGI9UVTZYEYp4'
    access_token_key = '863484896546770945-CsE61AWAUyEHbYCwK9ufdFPZsLvaFHu'
    access_token_secret = 'AGuAmkuGPfEEJEN865d5b5PLxKUlGDKlbguLtSH6gZiX0'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    auth_api = API(auth)
    return auth_api


# Fetch the recent tweets of a user
def fetch_tweets(auth_api, username):
    # For a day before
    yesterday = str(datetime.now() - timedelta(1))
    yesterday = list(map(int, re.split('\W+', yesterday)))
    startDate = datetime(
        yesterday[0], yesterday[1], yesterday[2]-1, yesterday[3], yesterday[4], yesterday[5])
    # Current day
    nowtime = str(datetime.now())
    nowtime = list(map(int, re.split('\W+', nowtime)))
    endDate = datetime(nowtime[0], nowtime[1],
                       nowtime[2], nowtime[3], nowtime[4], nowtime[5])
    tweets = []
    tmpTweets = auth_api.user_timeline(username)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

    while (tmpTweets[-1].created_at > startDate):
        tmpTweets = auth_api.user_timeline(
            username, max_id=tmpTweets[-1].id)
        for tweet in tmpTweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                tweets.append(tweet)
    res = []
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        res.append(tweet.text)
    return res


auth = authenticate()
username = input('Enter your username:\t')
print("Please Wait... \n")

tweets = fetch_tweets(auth, username)
s = pd.Series(tweets)
print("Fetched Successfully")

data = pd.DataFrame({'Tweets': s})
data.to_csv("Recent Tweets.csv", index=False)
