from pathlib import Path

# ---------------------------
# BASE DIRECTORIES
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# AGENTS
# ---------------------------

AGENTS_DIR = BASE_DIR / "agents"

LINUX_LOG = AGENTS_DIR / "linux" / "auth.log"

AIX_LOG = AGENTS_DIR / "aix" / "sudo.log"

# ---------------------------
# THREAT INTELLIGENCE
# ---------------------------

THREAT_INTEL_DIR = BASE_DIR / "threat-intelligence"

THREAT_FEED = THREAT_INTEL_DIR / "threat-feed.json"

IOC_FEED = THREAT_INTEL_DIR / "ioc-feed.json"

# ---------------------------
# DATABASE
# ---------------------------

DATABASE_DIR = BASE_DIR / "database"

DATABASE_PATH = DATABASE_DIR / "security.db"

# ---------------------------
# DETECTIONS
# ---------------------------

DETECTIONS_DIR = BASE_DIR / "detections"

SIGMA_RULES_DIR = DETECTIONS_DIR / "sigma"

FALCO_RULES = DETECTIONS_DIR / "falco-rules.yaml"

# ---------------------------
# REPORTS
# ---------------------------

REPORTS_DIR = BASE_DIR / "reports"

# ---------------------------
# LOGS
# ---------------------------

LOGS_DIR = BASE_DIR / "logs"

# ---------------------------
# CREATE REQUIRED DIRECTORIES
# ---------------------------

DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)

LOGS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# APPLICATION MODES
# ---------------------------

SIMULATION_MODE = True

REALTIME_MONITORING = True

ENABLE_THREAT_INTEL = True

ENABLE_CLOUD_MONITORING = True

ENABLE_SOAR = True

# ---------------------------
# COLLECTOR SETTINGS
# ---------------------------

LINUX_LOG_PATH = "/var/log/auth.log"

AIX_LOG_PATH = "/var/log/auth.log"

COLLECT_INTERVAL_SECONDS = 30

# ---------------------------
# SSH COLLECTION
# ---------------------------

SSH_TIMEOUT = 10

SSH_PORT = 22

# ---------------------------
# STREAMLIT
# ---------------------------

PAGE_TITLE = "Enterprise Security Operations Platform"

PAGE_ICON = "🛡️"

LAYOUT = "wide"
