import tweepy
import pandas as pd
import numpy as np

# Authenticate to Twitter
auth = tweepy.OAuthHandler("0KL6is2jkGPfE4y8dtCIA4yF5", "8E5PXkQYdrxmCZLXlW1xJOZEEOZjxrajt94IoxIbXbNAecwks2")
auth.set_access_token("733661563081527296-xAm980QpXaACI0HHf4XOGnogVAxZXDm", "jgkEHhIHD6rGZPMiyZ9ZODYsSnPAdNZh6UOWc6qonSy9u")

# Create API object
api = tweepy.API(auth)

# bring in the quote list
quote_df = pd.read_csv('Quote List.csv')
rand = np.random.randint(0, len(quote_df))
rand_quote = quote_df.iloc[rand]['quotes']

# Create a tweet
api.update_status(rand_quote)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")