import json

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient


auth_credential = DefaultAzureCredential()
scopes = ['application.readwrite.all']
client = GraphClient(credential=auth_credential)


def delete_secret_to_azure_ad_app():
    object_id = '00000000-0000-0000-0000-000000000000'
    # keyId is the Secret ID for the Azure AD application
    # https://docs.microsoft.com/en-us/graph/api/application-removepassword?view=graph-rest-1.0&tabs=http
    post_body = {
        'keyId': '00000000-0000-0000-0000-000000000000'
    }
    print(post_body)
    client.post(
        f'/applications/{object_id}/removePassword',
        data = json.dumps(post_body),
        headers={'Content-Type': 'application/json'}
    )

    print(f"Deleted key with keyId {post_body['keyId']}")


delete_secret_to_azure_ad_app()