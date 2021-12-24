import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

# Ref: https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications
credential = DefaultAzureCredential()

# Retrieve subscription ID from environment variable
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

RESOURCE_GROUP_NAME = 'PythonSDK-RG'
LOCATION = "eastus"

resource_client = ResourceManagementClient(credential, subscription_id)
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
    { "location": LOCATION })

print(f"Provisioned resource group {rg_result.name}")

SERVICE_PLAN_NAME = 'PythonSDK-ASP'

app_service_client = WebSiteManagementClient(credential, subscription_id)

# Provision the plan; Linux is the default
poller = app_service_client.app_service_plans.begin_create_or_update(RESOURCE_GROUP_NAME,
    SERVICE_PLAN_NAME,
    {
        "location": LOCATION,
        "reserved": True,
        "sku" : {"name" : "B1"}
    }
)

plan_result = poller.result()
print(f"Provisioned App Service plan {plan_result.name}")
