import os

RESOURCE = "https://graph.microsoft.com"  
TENANT_ID = os.getenv("TENANT_ID") 
AUTHORITY_HOST_URL = "https://login.microsoftonline.com"
CLIENT_ID = os.getenv("CLIENT_ID")  
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  

# These settings are for the Microsoft Graph API Call
API_VERSION = 'v1.0'
