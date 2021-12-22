import os
from azure.identity import DefaultAzureCredential

from azure.storage.blob import BlobClient

# Ref: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications#how-to-use-defaultazurecredential-when-accessing-resources
credential = DefaultAzureCredential()

# Retrieve the storage blob service URL, which is of the form
# https://pythonsdkstorage12345.blob.core.windows.net/
storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]

blob_client = BlobClient(storage_url, container_name="general-container", blob_name="pythonsdksample.txt", credential=credential)
print(storage_url)
with open("./sample.txt", "rb") as data:
    blob_client.upload_blob(data)