from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
import logging
import uuid

# Creates an authenticated client to the Azure Text Analytics Service

def authenticate_client():
    ta_credential = AzureKeyCredential(os.environ["TextAnalyticsKey"])
    text_analytics_client = TextAnalyticsClient(
            endpoint=os.environ["TextanalyticsEndpoint"], 
            credential=ta_credential)
    return text_analytics_client

def analyze_statement(statement, client: TextAnalyticsClient):
    try:
        # Message argument has to be an array to feed to the sentiment analysis api
        response = client.analyze_sentiment(documents=[statement])

        docs = [doc for doc in response if not doc.is_error]
        analyzed_data = {}

        logging.info("Logging the sentiment of the received statements")
        for idx, doc in enumerate(docs):
            logging.info("Document text: {}".format([statement][idx]))
            logging.info("Overall sentiment: {}".format(doc.sentiment))

            logging.info("Formatting response...")
            sentiment_values = {}
            sentiment_values["positive"] = doc.confidence_scores.positive
            sentiment_values["neutral"] = doc.confidence_scores.neutral
            sentiment_values["negative"] = doc.confidence_scores.negative
            analyzed_data["message"] = [statement][idx]
            analyzed_data["sentiment"] = doc.sentiment
            analyzed_data["sentimentValues"] = sentiment_values
            analyzed_data["rowKey"] = str(uuid.uuid4())
        
        return analyzed_data
    except Exception as err:
        logging.error(f"Unable to analyze dataset. Details {err}")
        raise 
    

