from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def list_azure_service_principals():
    # List Service Principals
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-list?view=graph-rest-1.0&tabs=http
    result = client.get(
        '/servicePrincipals',
    )

    # Drill down into the returned result. The top level result may be large depending on the organization
    for r in result.json()['value']:
        print(r['displayName'])

list_azure_service_principals()