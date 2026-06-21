from parsers.cmdb_engine import (
    load_cmdb
)

from parsers.asm_engine import (
    load_external_assets
)

# --------------------------------
# SHADOW IT
# --------------------------------

def detect_shadow_it():

    cmdb = load_cmdb()

    assets = load_external_assets()

    cmdb_hosts = [

        asset["hostname"]

        for asset in cmdb

    ]

    findings = []

    for asset in assets:

        if asset["hostname"] not in cmdb_hosts:

            findings.append(asset)

    return findings
