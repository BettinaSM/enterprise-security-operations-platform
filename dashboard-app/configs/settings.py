from pathlib import Path

# ---------------------------
# BASE PATHS
# ---------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

AGENTS_DIR = BASE_DIR / "agents"

LOGS_DIR = BASE_DIR / "logs"

DATABASE_DIR = BASE_DIR / "database"

# ---------------------------
# EXECUTION MODE
# ---------------------------

SIMULATION_MODE = True

# False = coleta real
# True = usar logs simulados

# ---------------------------
# LINUX
# ---------------------------

LINUX_AUTH_LOG = AGENTS_DIR / "linux" / "auth.log"

REAL_LINUX_AUTH_LOG = "/var/log/auth.log"

# ---------------------------
# AIX
# ---------------------------

AIX_SUDO_LOG = AGENTS_DIR / "aix" / "sudo.log"

# ---------------------------
# THREAT INTEL
# ---------------------------

THREAT_FEED = (
    BASE_DIR
    / "threat-intelligence"
    / "threat-feed.json"
)
