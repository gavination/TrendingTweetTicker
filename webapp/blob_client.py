import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv, main


def upload_blob(filepath: str, connection_string: str, filename: str, blob_container_name: str):
    try:
        print ("Blob client runtime testing...")
        load_dotenv()

        # Getting blob storage connection credentials.
        # connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
        # container_name= os.environ["CONTAINER_NAME"]
        # local_file_name = "saved_tweets.csv"

        upload_file_path = os.path.join(filepath, filename)

        # creating the client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # upload file to blob storage
        blob_client = blob_service_client.get_blob_client(container=blob_container_name, blob=filename)

        print("\nUploading to Azure Storage as blob:\n\t" + filename)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

    except Exception as ex:
        print('Exception:')
        print(ex)


if __name__ == "__main__":
    upload_blob("data")
    



