# Terraform Cloud Version Manager

This tiny script makes it easy to update the Terraform Version on all of the Workspaces inside Terraform Cloud. It will load a list of Worksapces for an Organization and set their versions to either the latest Terraform version or whatever is specified.

## Installation

```bash
git clone git@github.com:tedivm/tfc_version.git
cd tfc_version
poetry install
```

## Authentication

This project uses the same credentials file as `terraform` itself. If you haven't already run `terraform login` before using this tool.

You can also set the `TFC_TOKEN` environment variable.

To use a custom install of Terraform Enterprise set the environment variable TFC_DOMAIN to the domain of your instance (just the domain without the `http` portion of the URL or any trailing slashes, ie `app.terraform.io`).

## Usage

If you used Poetry to install replace `tfc_version` with `poetry run tfc_version`.

### List Workspaces

```bash
tfc_version list ORGANIZATION_NAME
```

### Upgrade to Latest

```bash
tfc_version set-version ORGANIZATION_NAME
```

### Upgrade to Specific Version

```bash
tfc_version set-version ORGANIZATION_NAME 1.1.2
```

### List Terraform Versions

```bash
tfc_version list-available-verions
```

### Get Lastest Version

```bash
tfc_version get-latest-version
```
