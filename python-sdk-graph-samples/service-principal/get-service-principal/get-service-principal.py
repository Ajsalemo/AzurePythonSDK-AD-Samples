from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def get_service_principal():
    # Get a Service Principal
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-get?view=graph-rest-1.0&tabs=http
    service_principal_id = '00000000-0000-0000-0000-0000000000'

    result = client.get(
        f'/servicePrincipals/{service_principal_id}',
    )

    print(result.json())

get_service_principal()