from twython import Twython
from dotenv import load_dotenv


import pandas as pd
import json
import os 

# Load credentials from json file

# Instantiate an object
load_dotenv()

python_tweets = Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

# Create our query
query = {'q': 'Kanye West Kim Kardashian West',
        'result_type': 'recent',
        'count': 10,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

print(df)