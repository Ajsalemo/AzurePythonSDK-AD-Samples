from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient


auth_credential = DefaultAzureCredential()
scopes = ['application.readwrite.all']
client = GraphClient(credential=auth_credential)


def delete_azure_ad_app():
    # https://docs.microsoft.com/en-us/graph/api/application-delete?view=graph-rest-1.0&tabs=http
    object_id = '00000000-0000-0000-0000-000000000000'
    client.delete(
        f'/applications/{object_id}',
    )

    print(f"Deleted Service Principal with Object ID {object_id}")


delete_azure_ad_app()