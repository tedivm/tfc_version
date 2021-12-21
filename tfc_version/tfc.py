import json
import os
from pathlib import Path

from terrasnek.api import TFC

TFC_TOKEN = os.getenv("TFC_TOKEN", False)
TFC_SSL_VERIFY = os.getenv("TFC_SSL_VERIFY", True)
TFC_DOMAIN = os.getenv("TFC_DOMAIN", "app.terraform.io")
TFC_URL = os.getenv("TFC_URL", f"https://{TFC_DOMAIN}")

credentials_path = Path.home() / ".terraform.d" / "credentials.tfrc.json"
if credentials_path.exists():
    cred_data = json.loads(credentials_path.read_bytes())
    token = cred_data.get("credentials", {}).get(TFC_DOMAIN, {}).get("token", False)
    if token:
        TFC_TOKEN = token

if not TFC_TOKEN:
    raise Exception("TFC Token Required")


api = TFC(TFC_TOKEN, url=TFC_URL, verify=TFC_SSL_VERIFY)


def update_workspace_version(organization, workspace_id, version):
    api.set_org(organization)
    payload = {
        "data": {
            "type": "workspace",
            "attributes": {
                "terraform_version": version,
            },
        }
    }
    api.workspaces.update(payload, workspace_id=workspace_id)


def get_workspaces(organization):
    api.set_org(organization)
    response = api.workspaces.list_all()
    data = response["data"]
    data.sort(key=lambda x: x["attributes"]["name"])
    return data
