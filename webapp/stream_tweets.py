from twython import TwythonStreamer
import os, uuid
import logging
from dotenv import load_dotenv
from storage_client import queue_message

# Filter out unwanted data
# Commented fields i don't need yet, but might later
def process_tweet(tweet):
    d = {}
    # d["hashtags"] = [hashtag["text"] for hashtag in tweet["entities"]["hashtags"]]
    d["text"] = tweet["text"]
    # d["user"] = tweet["user"]["screen_name"]
    # d["user_loc"] = tweet["user"]["location"]
    return d

class StreamAgent(TwythonStreamer):     

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data["lang"] == "en":
            tweet_data = process_tweet(data)
            self.write_to_queue(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        logging.error(status_code, data)
        self.disconnect()
        
    # Save each tweet to a text file
    # todo: figure out how to stream files directly to blob storage...eventually
    def save_to_txt(self, tweet):
        with open(r"saved_ tweets.txt", "a") as file:
            file.writelines(list(tweet.values()))
    
    def write_to_queue(self, tweet):
        queue_message(tweet)


if __name__ == "__main__":
    load_dotenv()

    stream = StreamAgent(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], 
                        os.environ["ACCESS_TOKEN"], os.environ["ACCESS_SECRET"])
    # Start the stream
    stream.statuses.filter(track="Kanye West Kim Kardashian West divorce" )