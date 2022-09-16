import json

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

auth_credential = DefaultAzureCredential()
client = GraphClient(credential=auth_credential)

def delete_secret_of_service_principal():
    # Delete a password/secret to a Service Principal
    # https://docs.microsoft.com/en-us/graph/api/serviceprincipal-addpassword?view=graph-rest-1.0&tabs=http
    service_principal_id = '00000000-0000-0000-0000-0000000000'
    # GUID of the secret itself
    body = {
        'keyId': '00000000-0000-0000-0000-0000000000' 
    }
    
    client.post(
        f'/servicePrincipals/{service_principal_id}/removePassword',
        data = json.dumps(body),
        headers = {'Content-Type': 'application/json'}
    )

    print(f'Deleted secret with ID: {body["keyId"]}')

delete_secret_of_service_principal()