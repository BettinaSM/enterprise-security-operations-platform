from pathlib import Path

# ---------------------------
# BASE DIR
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# APPLICATION
# ---------------------------

APP_NAME = "Enterprise Security Operations Platform"

# ---------------------------
# DIRECTORIES
# ---------------------------

SIMULATIONS_DIR = BASE_DIR / "simulations"

THREAT_INTEL_DIR = BASE_DIR / "threat-intelligence"

RULES_DIR = BASE_DIR / "detections" / "rules"

LOGS_DIR = BASE_DIR / "logs"

DATABASE_DIR = BASE_DIR / "database"

REPORTS_DIR = BASE_DIR / "reports"

# ---------------------------
# DATABASE
# ---------------------------

DB_PATH = DATABASE_DIR / "security.db"
