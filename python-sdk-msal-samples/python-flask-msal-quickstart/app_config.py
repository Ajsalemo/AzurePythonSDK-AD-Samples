import os
# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Client Secret of app registration
CLIENT_SECRET = os.getenv("CLIENT_SECRET") 
AUTHORITY = "https://login.microsoftonline.com/common"  
# The absolute URL must match the redirect URI you set in the app's registration in the Azure portal.
REDIRECT_PATH = os.getenv("REDIRECT_PATH")  

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
# This resource requires no admin consent
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]
# Specifies the token cache should be stored in server-side sessio
SESSION_TYPE = "filesystem"  
