# Delete a secret on an Azure AD Application

This sample uses the [Microsoft Graph Core Python Client Library (preview)](https://github.com/microsoftgraph/msgraph-sdk-python-core).

This example deletes a secret (password) on an Azure AD application through this API's endpoint - [Delete a Secret](https://docs.microsoft.com/en-us/graph/api/application-removepassword?view=graph-rest-1.0&tabs=http)

## Running the sample
- Before running the sample, make sure your local environment is set up correctly. You'll need to either create or use an existing Service Principal. You can follow this [link](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd) on how to create a Service Principal.
When using this Python SDK, `DefaultAzureCredential` expects `AZURE_SUBSCRIPTION_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` and `AZURE_TENANT_ID` to be available. This is called out [here](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#create-a-service-principal-and-environment-variables-for-development).
- Create and activate your virtual environment and run `delete-secret-to-azure-ad-app.py`.
