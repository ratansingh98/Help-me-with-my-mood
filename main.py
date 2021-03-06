import pandas as pd
# Fetching Tweets from user
import fetch_tweet

# Load tweets
tweets = pd.read_csv("Recent Tweets.csv").iloc[:, 0]

# Obtain a model if doesn't exists
import os
if not os.path.exists("model.sav"):
    print("\nWait for model training")
    import train_model


# Predict tweet
import predict
from predict import predict_tweet
res = []
for tweet in tweets:
    tweet = tweet.replace('\n', ' ')
    res.append(predict_tweet(tweet)[0])

today_mood = max(res)
print("\nYour today emotion is", today_mood)

# Recommend a song
print("\nChoosing a song for you")
from play_song import playSong
playSong(today_mood)
