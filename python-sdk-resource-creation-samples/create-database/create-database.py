import random, os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.rdbms.mysql import MySQLManagementClient
from azure.mgmt.rdbms.mysql.models import ServerForCreate, ServerPropertiesForDefaultCreate, ServerVersion

# Reference - https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate-hosted-applications#how-to-use-defaultazurecredential-when-accessing-resources
credential = DefaultAzureCredential()

# Retrieve subscription ID from environment variable
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

RESOURCE_GROUP_NAME = 'PythonAzureExample-DB-rg'
LOCATION = "eastus"

resource_client = ResourceManagementClient(credential, subscription_id)
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
    { "location": LOCATION })

print(f"Provisioned resource group {rg_result.name}")

db_server_name = os.environ.get("DB_SERVER_NAME", f"PythonAzureExample-MySQL-{random.randint(1,100000):05}")
db_admin_name = os.environ.get("DB_ADMIN_NAME", "azureuser")
db_admin_password = os.environ.get("DB_ADMIN_PASSWORD", "ChangePa$$w0rd24")

mysql_client = MySQLManagementClient(credential, subscription_id)

# Provision the server and wait for the result
poller = mysql_client.servers.begin_create(RESOURCE_GROUP_NAME,
    db_server_name, 
    ServerForCreate(
        location=LOCATION,
        properties=ServerPropertiesForDefaultCreate(
            administrator_login=db_admin_name,
            administrator_login_password=db_admin_password,
            version=ServerVersion.FIVE7
        )
    )
)

server = poller.result()
print(f"Provisioned MySQL server {server.name}")

# Provision a firewall rule to allow the local workstation to connect
RULE_NAME = "allow_ip"
ip_address = os.environ["PUBLIC_IP_ADDRESS"]

# For the above code, create an environment variable named PUBLIC_IP_ADDRESS that
# contains your workstation's public IP address as reported by a site like
# https://whatismyipaddress.com/.

# Provision the rule and wait for completion
poller = mysql_client.firewall_rules.begin_create_or_update(RESOURCE_GROUP_NAME,
    db_server_name, RULE_NAME, 
    { "start_ip_address": ip_address, "end_ip_address": ip_address }  
)

firewall_rule = poller.result()
print(f"Provisioned firewall rule {firewall_rule.name}")

db_name = os.environ.get("DB_NAME", "example-db1")
poller = mysql_client.databases.begin_create_or_update(RESOURCE_GROUP_NAME,
    db_server_name, db_name, {})

db_result = poller.result()
print(f"Provisioned MySQL database {db_result.name} with ID {db_result.id}")