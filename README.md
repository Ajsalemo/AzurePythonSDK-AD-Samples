# AzurePythonSDK-AD-Samples

Various samples for utilizing the Azure Python SDK with AAD.

This repository contains the following examples. Each example contains an additional `README` that explains how to run the sample:
- `python-sdk-resource-creation-samples` - samples for various resource creation
- `python-sdk-msi-samples` - various Managed Identity Service (MSI) samples
- `python-sdk-msal-samples` - various MSAL samples
- `python-sdk-adal-samples` - various ADAL samples
- `python-sdk-graph-samples` - various Graph API samples

> **NOTE**: The python-sdk-graph-samples use a preview library. The previously used SDK, [Azure Active Directory Graph libraries for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/microsoft-graph?view=azure-python) have not been updated since 2019 and can be deemed deprecated. If the preview libraries are not able to be used for whatever reason, utilize the Graph API (See README.md's in said samples for documentation on those calls) - which is what the new samples call under the hood.
