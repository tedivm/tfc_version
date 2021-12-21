import sys

import semver
import typer

from .terraform import LATEST_VERSION, VERSIONS
from .tfc import api, get_workspaces, update_workspace_version

app = typer.Typer()


@app.command()
def main(name: str):
    for workspace in api.workspaces._list_all():
        typer.echo(workspace)


@app.command()
def list(organization: str):
    data = get_workspaces(organization)
    for workspace in data:
        typer.echo(f'{workspace["attributes"]["name"]} ({workspace["id"]})')


@app.command()
def list_available_versions():
    for version in VERSIONS:
        typer.echo(version)


@app.command()
def get_latest_version():
    typer.echo(LATEST_VERSION)


@app.command()
def set_version(organization: str, version: str = str(LATEST_VERSION)):

    test_version = semver.VersionInfo.parse(version)

    if not test_version in VERSIONS:
        typer.echo("Version not in available version list.")
        sys.exit(1)

    data = get_workspaces(organization)
    for workspace in data:
        typer.echo(
            f'{workspace["attributes"]["name"]} ({workspace["id"]}) to {version}'
        )
        update_workspace_version(organization, workspace["id"], version)


if __name__ == "__main__":
    app()
