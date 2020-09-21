import tweepy
import pandas as pd
import numpy as np
import json

def get_keys(path):
    with open(path) as f:
        return json.load(f)

#retrieve the relevant keys
keys = get_keys('api_keys.json')
consumer_key = keys['tw_consumer_key']
consumer_secret = keys['tw_consumer_secret']
access_token = keys['tw_access_token']
access_secret = keys['tw_access_secret']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create API object
api = tweepy.API(auth)

# bring in the quote list and find a random quote
quote_df = pd.read_csv('Quote List.csv')
rand = np.random.randint(0, len(quote_df))
rand_quote = quote_df.iloc[rand]['quotes']

# send the tweet
api.update_status(rand_quote)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")