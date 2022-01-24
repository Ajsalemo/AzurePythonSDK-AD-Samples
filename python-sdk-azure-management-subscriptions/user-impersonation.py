#Python implementation of Subscription Client similar to https://docs.microsoft.com/en-us/rest/api/resources/tenants/list
#Authentication using Username and Password with UsernamePasswordCredential library

TenantId= '*****'
AppId= '*****'
user = '*****'
password = '*****'

from azure.identity import UsernamePasswordCredential
from azure.mgmt.resource.subscriptions import SubscriptionClient

credential = UsernamePasswordCredential(AppId,user,password,tenant_id=TenantId)
subscription_client = SubscriptionClient(credential,api_version='2021-01-01')
tenants = subscription_client.tenants.list()
access_token = credential.get_token("https://management.azure.com/.default").token

print("ClientSecretCredential Token:\r\n")
print(access_token)
print("\r\n")
print("Tenant Information:\r\n")
for t in tenants:
    print(t)