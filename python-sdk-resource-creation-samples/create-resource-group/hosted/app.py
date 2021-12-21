from flask import Flask, jsonify
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Python-SDK-Resource-Creation-Samples"


@app.route("/create")
def create():
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    resource_client = ResourceManagementClient(credential, subscription_id)

    rg_result = resource_client.resource_groups.create_or_update(
        "PythonAzureExample-rg",
        {
            "location": "centralus"
        }
    )

    print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

    rg_result = resource_client.resource_groups.create_or_update(
        "PythonAzureExample-rg",
        {
            "location": "centralus",
            "tags": { "environment":"test", "department":"tech" }
        }
    )

    print(f"Updated resource group {rg_result.name} with tags")
    return jsonify({ "message": f"Created Resource Group: {rg_result.name} "})
