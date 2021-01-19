from flask import Flask
from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from .check_twitter import search


app = Flask(__name__)

@app.route('/')
def display():
    return "Uatu, the Tweet Watcher...is watching."

def check_tweets():
    search()

if __name__=='__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_tweets, 'interval', seconds=2)
    scheduler.start()
    app.run()
