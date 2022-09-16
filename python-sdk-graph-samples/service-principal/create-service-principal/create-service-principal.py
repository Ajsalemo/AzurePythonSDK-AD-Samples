import json

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def create_service_principal():
    # Create a Service Principal
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-post-serviceprincipals?view=graph-rest-1.0&tabs=http
    # This is the appId of the owning Azure AD application
    body = {
        'appId': '00000000-0000-0000-0000-000000000000'
    }
    result = client.post(
        '/servicePrincipals',
        data = json.dumps(body),
        headers = {'Content-Type': 'application/json'}
    )

    print(result.json())


create_service_principal()