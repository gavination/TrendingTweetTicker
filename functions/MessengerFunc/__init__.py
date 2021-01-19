import json
import logging
from .utils import decider

import azure.functions as func

def main(documents: func.DocumentList, twilioMessage):

    logging.info("Messenger Function successfully invoked!")
    doc = documents[0].to_json()
    formatted_doc = json.loads(doc)
    
    sentiment = formatted_doc["sentiment"]
    message = formatted_doc["message"]

    logging.info("Deciding the stats...")
    text_message = decider.evaluate_sentiment(sentiment, message, 5043228579)

    twilioMessage.set(json.dumps(text_message))
    logging.info("Message sent")
 