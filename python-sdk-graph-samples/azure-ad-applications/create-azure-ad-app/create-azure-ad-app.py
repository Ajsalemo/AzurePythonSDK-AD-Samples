import json

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient


auth_credential = DefaultAzureCredential()
scopes = ['application.readwrite.all']
client = GraphClient(credential=auth_credential)


def create_azure_ad_app():
    # Display name of the Azure AD app that's being created
    # https://docs.microsoft.com/en-us/graph/api/application-post-applications?view=graph-rest-1.0&tabs=http
    post_body = {
            'displayName': 'newazureadapp'
    }

    result = client.post(
        '/applications',
        data = json.dumps(post_body),
        headers={'Content-Type': 'application/json'}
    )

    print(result.json())


create_azure_ad_app()