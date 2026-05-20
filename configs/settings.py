from pathlib import Path
import os

APP_NAME = "Unified Enterprise Security Operations Platform"

APP_VERSION = "1.0"

DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent

SIMULATIONS_DIR = BASE_DIR / "simulations"

RULES_DIR = BASE_DIR / "detections" / "sigma"

LOGS_DIR = BASE_DIR / "logs"

AGENTS_DIR = BASE_DIR / "agents"

THEME = os.getenv(
    "SOC_THEME",
    "dark"
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
