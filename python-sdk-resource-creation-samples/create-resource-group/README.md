# Create a Resource Group

This is sample is taken from [Use the Azure libraries to provision a resource group](https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-example-resource-group).

This sample uses the Azure Python SDK with [`DefaultAzureCredential`](https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications) to create a Resource Group.

## Running the sample
- Before running the sample, make sure your local environment is set up correctly. You'll need to either create or use an existing Service Principal. You can follow this [link](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd) on how to create a Service Principal.
When using this Python SDK, `DefaultAzureCredential` expects `AZURE_SUBSCRIPTION_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` and `AZURE_TENANT_ID` to be available. This is called out [here](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#create-a-service-principal-and-environment-variables-for-development).
- Create and activate your virtual environment and run `python create-resource-group.py`.
