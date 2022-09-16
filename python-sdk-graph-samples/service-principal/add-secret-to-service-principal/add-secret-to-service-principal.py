from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def add_secret_to_service_principal():
    # Add a password/secret to a Service Principal
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-addpassword?view=graph-rest-1.0&tabs=http
    service_principal_id = '00000000-0000-0000-0000-0000000000'

    result = client.post(
        f'/servicePrincipals/{service_principal_id}/addPassword',
        headers = {'Content-Type': 'application/json'}
    )

    print(result.json())

add_secret_to_service_principal()