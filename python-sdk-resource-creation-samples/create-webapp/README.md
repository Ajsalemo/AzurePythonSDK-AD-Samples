# Create a Web App

This sample uses the Azure Python SDK with [`DefaultAzureCredential`](https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications) to create a Web App.

## Running the sample
- Before running the sample, make sure your local environment is set up correctly. You'll need to either create or use an existing Service Principal. You can follow this [link](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd) on how to create a Service Principal.
When using this Python SDK, `DefaultAzureCredential` expects `AZURE_SUBSCRIPTION_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` and `AZURE_TENANT_ID` to be available. This is called out [here](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#create-a-service-principal-and-environment-variables-for-development).
- Prior to Web App creation, this SDK creates a Resource Group and App Service Plan. This can be changed to target an existing Resource Group or App Service Plan if desired.
- Create and activate your virtual environment and run `python create-webapp.py`.
