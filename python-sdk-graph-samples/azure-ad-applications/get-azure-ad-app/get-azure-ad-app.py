from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient


auth_credential = DefaultAzureCredential()
scopes = ['application.read.all']
client = GraphClient(credential=auth_credential)


def get_azure_ad_app():
    # https://docs.microsoft.com/en-us/graph/api/application-get?view=graph-rest-1.0&tabs=http
    object_id = '00000000-0000-0000-0000-000000000000'
    result = client.get(
        f'/applications/{object_id}',
    )

    print(result.json()['displayName'])


get_azure_ad_app()