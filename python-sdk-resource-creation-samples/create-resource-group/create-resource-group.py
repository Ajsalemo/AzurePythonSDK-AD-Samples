from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
import os

# Reference - https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications#how-to-use-defaultazurecredential-when-accessing-resources
credential = DefaultAzureCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

resource_client = ResourceManagementClient(credential, subscription_id)

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "eastus"
    }
)

print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "eastus",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")

