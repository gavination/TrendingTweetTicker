from dotenv.main import load_dotenv
from stream_tweets import StreamAgent
from flask import Flask
from datetime import datetime
import time
import os

from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

@app.route('/')
def display():
    return "Uatu, the Tweet Watcher...is watching."

def check_tweets():
    stream = StreamAgent(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], 
                        os.environ["ACCESS_TOKEN"], os.environ["ACCESS_SECRET"])
        # Start the stream
    stream.statuses.filter(track=os.environ["SEARCH_TERMS"])

if __name__=='__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(check_tweets, 'interval', hours=2, replace_existing=True)
    # scheduler.start()
    load_dotenv()
    check_tweets()
    app.run()
