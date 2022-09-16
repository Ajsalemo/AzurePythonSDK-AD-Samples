from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def delete_service_principal():
    # Delete a Service Principal
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-delete?view=graph-rest-1.0&tabs=http
    service_principal_id = '00000000-0000-0000-0000-0000000000'

    client.delete(
        f'/servicePrincipals/{service_principal_id}',
    )

    print(f'Deleted Service Principle with ID: {service_principal_id}')

delete_service_principal()