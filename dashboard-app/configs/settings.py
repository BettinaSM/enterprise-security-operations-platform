from pathlib import Path

APP_NAME = "Unified Enterprise Security Operations Platform"

BASE_DIR = Path(__file__).resolve().parent.parent

SIMULATIONS_DIR = BASE_DIR / "simulations"

RULES_DIR = BASE_DIR / "detections" / "sigma"

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
