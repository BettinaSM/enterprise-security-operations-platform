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

from configs.settings import (
    THREAT_INTEL_DIR
)

threat_feed = load_threat_feed(
    THREAT_INTEL_DIR / "threat-feed.json"
)

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
