import os

from azure.identity import ManagedIdentityCredential
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

CLIENT_ID = os.getenv('CLIENT_ID')

def user_assigned_msi():
    # You can create a User Assigned Identity and assign it with the following: https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/qs-configure-cli-windows-vm#:~:text=Assign%20User%20Assigned%20Identity%20during%20the%20Creation%20of,VM%20using%20az%20vm%20create.%20...%20See%20More.
    # Create User Assigned MSI Authentication instance
    credentials = ManagedIdentityCredential(
        client_id=CLIENT_ID
    )

    subscription_client = SubscriptionClient(credentials)
    subscription = next(subscription_client.subscriptions.list())
    subscription_id = subscription.subscription_id
    resource_client = ResourceManagementClient(credentials, subscription_id)
    for resource_group in resource_client.resource_groups.list():
        print(resource_group.name)


if __name__ == "__main__":
    user_assigned_msi()
