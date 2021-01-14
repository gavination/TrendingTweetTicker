from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
import logging

# Creates an authenticated client to the Azure Text Analytics Service

def authenticate_client():
    ta_credential = AzureKeyCredential(os.environ["TextAnalyticsKey"])
    text_analytics_client = TextAnalyticsClient(
            endpoint=os.environ["TextanalyticsEndpoint"], 
            credential=ta_credential)
    return text_analytics_client

    # Message argument has to be an array to feed to the sentiment analysis api
def analyze_statement(statement, client: TextAnalyticsClient):
    response = client.analyze_sentiment(documents=[statement])

    docs = [doc for doc in response if not doc.is_error]

    logging.info("Logging the sentiment of the received statements")
    for idx, doc in enumerate(docs):
        logging.info("Document text: {}".format([statement][idx]))
        logging.info("Overall sentiment: {}".format(doc.sentiment))
