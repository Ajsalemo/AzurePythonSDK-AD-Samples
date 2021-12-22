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
WEB_APP_NAME = os.environ.get("WEB_APP_NAME")

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

poller = app_service_client.web_apps.begin_create_or_update(RESOURCE_GROUP_NAME,
    WEB_APP_NAME,
    {
        "location": LOCATION,
        "server_farm_id": plan_result.id,
        "site_config": {
            "linux_fx_version": "python|3.8"
        }
    }
)

web_app_result = poller.result()
print(f"Provisioned web app {web_app_result.name} at {web_app_result.default_host_name}")

# Step 4: deploy code from a GitHub repository. For Python code, App Service on Linux runs
# the code inside a container that makes certain assumptions about the structure of the code.
# For more information, see How to configure Python apps,
# https://docs.microsoft.com/azure/app-service/containers/how-to-configure-python.
#
# The create_or_update_source_control method doesn't provision a web app. It only sets the
# source control configuration for the app. In this case we're simply pointing to
# a GitHub repository.
#
# You can call this method again to change the repo.

REPO_URL = os.environ["REPO_URL"]

poller = app_service_client.web_apps.begin_create_or_update_source_control(RESOURCE_GROUP_NAME,
    WEB_APP_NAME, 
    { 
        "location": "GitHub",
        "repo_url": REPO_URL,
        "branch": "main"
    }
)

sc_result = poller.result()

print(f"Set source control on web app to {sc_result.branch} branch of {sc_result.repo_url}")