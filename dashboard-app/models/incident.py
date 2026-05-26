from dataclasses import dataclass

@dataclass
class Incident:

    severity: str

    source: str

    description: str

    status: str
