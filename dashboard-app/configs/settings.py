from pathlib import Path

APP_NAME = "Unified Enterprise Security Operations Platform"

BASE_DIR = Path(__file__).resolve().parent.parent

SIMULATIONS_DIR = BASE_DIR / "simulations"

LOGS_DIR = BASE_DIR / "logs"

DATABASE_DIR = BASE_DIR / "database"

REPORTS_DIR = BASE_DIR / "reports"

THREAT_INTEL_DIR = BASE_DIR / "threat-intelligence"

RULES_DIR = BASE_DIR / "detections" / "sigma"

AGENTS_DIR = BASE_DIR.parent / "agents"

THREAT_FEED_DIR = BASE_DIR / "threat-intelligence"

SUPPORTED_ENVIRONMENTS = [
    "Linux",
    "AIX",
    "Windows",
    "AWS",
    "Azure",
    "GCP",
    "OCI",
    "IBM Cloud",
    "Kubernetes"
]
