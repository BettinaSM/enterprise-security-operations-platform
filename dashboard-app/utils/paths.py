from pathlib import Path

# --------------------------------
# BASE
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------
# DIRECTORIES
# --------------------------------

SIMULATIONS_DIR = BASE_DIR / "simulations"
THREAT_INTEL_DIR = BASE_DIR / "threat-intelligence"
THREAT_DIR = BASE_DIR / "threat-intelligence"

LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
BASELINE_DIR = BASE_DIR / "baseline"
INVENTORY_DIR = BASE_DIR / "inventory"
VULN_DIR = BASE_DIR / "vulnerabilities"
CONTROL_DIR = BASE_DIR / "controls"

SECRETS_DIR = BASE_DIR / "secrets"
CONFIG_DIR = BASE_DIR / "configs"

# --------------------------------
# AUTO CREATE
# --------------------------------

for directory in [

    LOG_DIR,
    REPORT_DIR,
    BASELINE_DIR,
    INVENTORY_DIR,
    VULN_DIR,
    CONTROL_DIR

]:

    directory.mkdir(
        parents=True,
        exist_ok=True
    )
