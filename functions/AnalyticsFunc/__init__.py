import os
import json
import logging
import uuid
import requests
import azure.functions as func
from .utils import analytics_client

def main(inMessage: func.QueueMessage, outMessage: func.Out[func.Document]):
    logging.info('Python queue trigger function processed a queue item: %s',
                 inMessage.get_body().decode('utf-8'))
    
    try:
        row_key = str(uuid.uuid4())
        fetched_message = inMessage.get_body().decode('utf-8')
        client = analytics_client.authenticate_client()

        processed_data = analytics_client.analyze_statement(fetched_message, client, row_key)

        processed_msg = json.dumps(processed_data)
        outMessage.set(func.Document.from_json(processed_msg))
        logging.info(f"Message saved to CosmosDB with the row key: {row_key}")

    except Exception as err:
        logging.error(f"Something went wrong. Details: {err}")
        raise