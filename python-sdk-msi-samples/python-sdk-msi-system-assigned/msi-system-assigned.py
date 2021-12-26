from azure.identity import ManagedIdentityCredential
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

def system_assigned_msi():
    """MSI Authentication example."""

    # Create System Assigned MSI Authentication instance
    credentials = ManagedIdentityCredential()

    subscription_client = SubscriptionClient(credentials)
    subscription = next(subscription_client.subscriptions.list())
    subscription_id = subscription.subscription_id

    resource_client = ResourceManagementClient(credentials, subscription_id)

    for resource_group in resource_client.resource_groups.list():
        print(resource_group.name)


if __name__ == "__main__":
    system_assigned_msi()