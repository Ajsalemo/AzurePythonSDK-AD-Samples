# python-sdk-azure-management-subscription

This repository contains some examples to query tenant information from https://management.azure.com/

## Prerequisites
- [App Registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Choose from:
    - user-impersonation.py
        - User and password
        - Role User Impersonation Delegated permission on Azure Active Directory > App Registrations > API Permissions > Add a permission > Azure Service Management > user_impersonation > Add Permissions
        - Admin Consent from Azure Active Directory > App Registration > API Permissions > Grant Admin Consent
    - client-secret.py
        - Managed Identity
        - Client Secret created on Azure Active Directory > App Registration > Certificates & Secrets