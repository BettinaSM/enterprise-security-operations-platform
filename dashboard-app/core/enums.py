from enum import Enum


class Severity(Enum):

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class Environment(Enum):

    DEV = "Development"
    QA = "QA"
    HOM = "Homologation"
    PROD = "Production"
