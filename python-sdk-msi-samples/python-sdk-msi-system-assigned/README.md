# List Resource Groups on a VM with a System-Assigned Identity

This sample is generally taken from [here](https://github.com/Azure-Samples/resource-manager-python-manage-resources-with-msi) but has been changed to reflect the `ManagedIdentityCredential` class from the `azure-identity` library.

## Running the sample
- Set up a System-Assigned Identity for your Virtual Machine, which can be done [here](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal-managed-identity#system-assigned-managed-identity).
- Create and activate your virtual environment, run `pip install -r requirements.txt` and run `msi-system-assigned.py`.

### Troubleshooting
- If you have assigned a System-Assigned Identity but see a `StopIterator` exception, this most likely means the `next()` function has no subscriptions to iterate over. Review your permissions assigned to your System-Assigned Identity from your Virtual Machine.
- By default Identities no permisions which can be seen [here](https://github.com/Azure-Samples/compute-python-msi-vm#role-assignement-to-the-msi-credentials). If no Resource Groups are still printing, follow the documentation in the [link](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal-managed-identity#system-assigned-managed-identity) to set a Resource Group scope for the Identity.



