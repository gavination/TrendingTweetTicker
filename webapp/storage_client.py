import os, uuid
import logging
import base64
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv, main
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)


def upload_blob(filepath: str, connection_string: str, filename: str, blob_container_name: str):
    try:
        print ("Blob client runtime testing...")
        load_dotenv()

        upload_file_path = os.path.join(filepath, filename)

        # creating the client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # upload file to blob storage
        blob_client = blob_service_client.get_blob_client(container=blob_container_name, blob=filename)

        logging.info(f"\nUploading to Azure Storage as blob:\n\t {filename}")

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)
    except Exception as ex:
            logging.error(f'Exception uplaoding file to blob storage: {ex}')


def queue_message(message: str):
    try:
        queue_client = QueueClient.from_connection_string(os.environ["AZURE_STORAGE_CONNECTION_STRING"], 
                                                          os.environ["QUEUE_NAME"])

        logging.info(f"Adding message: {message}")
        
        encodedBytes = base64.b64encode(message.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")

        queue_client.send_message(encodedStr)

    except Exception as ex:
        logging.error(f"Exception uploading message to queue: {ex}")
