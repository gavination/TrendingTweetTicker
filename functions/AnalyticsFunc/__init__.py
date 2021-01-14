import logging
import json
import azure.functions as func
from .utils import analytics_client

def main(inMessage: func.QueueMessage, outMessage: func.Out[str]):
    logging.info('Python queue trigger function processed a queue item: %s',
                 inMessage.get_body().decode('utf-8'))
    
    fetched_message = inMessage.get_body().decode('utf-8')
    client = analytics_client.authenticate_client()

    processed_data = analytics_client.analyze_statement(fetched_message, client)

    proc = str(processed_data)
    outMessage.set(proc)
