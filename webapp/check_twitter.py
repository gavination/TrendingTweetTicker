from twython import Twython
from dotenv import load_dotenv, main
from storage_client import queue_message
import os 


def search_tweets(query: str):
    python_tweets = Twython(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

    query = {'q': query,
            'result_type': 'recent',
            'count': 10,
            'lang': 'en',
            }

    # Add tweets to queue
    for status in python_tweets.search(**query)['statuses']:
        queue_message(status["text"])


def write_to_queue(tweet):
    queue_message(tweet)

if __name__ == "__main__":
    load_dotenv()
    search_tweets("Kanye West Kim Kardashian West")