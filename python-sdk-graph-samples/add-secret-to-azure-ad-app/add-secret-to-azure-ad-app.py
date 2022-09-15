import json

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient


auth_credential = DefaultAzureCredential()
scopes = ['application.readwrite.all']
client = GraphClient(credential=auth_credential)


def add_secret_to_azure_ad_app():
    object_id = '00000000-0000-0000-0000-000000000000'
    # Display name is the 'friendly name' of the secret being created on this Service Principal
    # https://docs.microsoft.com/en-us/graph/api/application-addpassword?view=graph-rest-1.0&tabs=http
    post_body = {
        'passwordCredential': {
            'displayName': 'somefriendlyname'
        }
    }

    result = client.post(
        f'/applications/{object_id}/addPassword',
        data = json.dumps(post_body),
        headers={'Content-Type': 'application/json'}
    )

    print(result.json())


add_secret_to_azure_ad_app()