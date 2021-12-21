import os, random

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Python-SDK-Resource-Creation-Samples"


@app.route("/create")
def create():
    # See this on setting up a Service Principal/AD Application 
    # https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications#how-to-use-defaultazurecredential-when-accessing-resources
    credential = DefaultAzureCredential()

    # Retrieve subscription ID from environment variable.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

    resource_client = ResourceManagementClient(credential, subscription_id)

    RESOURCE_GROUP_NAME = "PythonAzureExample-Storage-rg"
    LOCATION = "eastus"
    STORAGE_ACCOUNT_NAME = f"pythonazurestorage{random.randint(1,100000):05}"

    rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
        { "location": LOCATION })

    print(f"Provisioned resource group {rg_result.name}")

    storage_client = StorageManagementClient(credential, subscription_id)
    availability_result = storage_client.storage_accounts.check_name_availability(
        { "name": STORAGE_ACCOUNT_NAME }
    )

    if not availability_result.name_available:
        print(f"Storage name {STORAGE_ACCOUNT_NAME} is already in use. Try another name.")
        exit()

    poller = storage_client.storage_accounts.begin_create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME,
        {
            "location" : LOCATION,
            "kind": "StorageV2",
            "sku": {"name": "Standard_LRS"}
        }
    )

    account_result = poller.result()
    print(f"Provisioned storage account {account_result.name}")


    # Step 3: Retrieve the account's primary access key and generate a connection string.
    keys = storage_client.storage_accounts.list_keys(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME)
    print(f"Primary key for storage account: {keys.keys[0].value}")

    conn_string = f"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={keys.keys[0].value}"
    print(f"Connection string: {conn_string}")

    CONTAINER_NAME = "blob-container-01"
    # The fourth argument is a required BlobContainer object, but because we don't need any special values there, so we just pass empty JSON.
    container = storage_client.blob_containers.create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {})

    print(f"Provisioned blob container {container.name}")
    return jsonify({ "message": f"created Resource Group named: {rg_result.name}, Storage Account named: {account_result.name} and Blob Container named: {container.name}" })
