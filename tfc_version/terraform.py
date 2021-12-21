import re

import httpx
import semver

response = httpx.get("https://releases.hashicorp.com/terraform/")
r"terraform_([\d|.|\-|rc|alpha|beta]+)"

VERSIONS = []

for result in re.finditer(r"terraform_([\d|.|\-|rc|alpha|beta]+)", response.text):
    verstring = result.groups()[0]
    if verstring.endswith("-"):
        continue
    version = semver.VersionInfo.parse(verstring)
    VERSIONS.append(version)

VERSIONS.sort(reverse=True)

for testing_version in VERSIONS:
    if testing_version.prerelease:
        continue
    LATEST_VERSION = testing_version
    break

VERSIONS.sort()
