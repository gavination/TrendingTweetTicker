import logging
import azure.functions as func
from .utils import analytics_client

def main(msg: func.QueueMessage) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    
    fetched_message = msg.get_body().decode('utf-8')
    client = analytics_client.authenticate_client()

    analytics_client.analyze_statement(fetched_message, client)