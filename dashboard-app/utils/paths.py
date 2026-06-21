from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SIMULATIONS_DIR = (
    BASE_DIR / "simulations"
)

THREAT_INTEL_DIR = (
    BASE_DIR / "threat-intelligence"
)

LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
BASELINE_DIR = BASE_DIR / "baseline"
INVENTORY_DIR = BASE_DIR / "inventory"
VULN_DIR = BASE_DIR / "vulnerabilities"
CONTROL_DIR = BASE_DIR / "controls"
THREAT_DIR = BASE_DIR / "threat-intelligence"

LOG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
BASELINE_DIR.mkdir(exist_ok=True)
