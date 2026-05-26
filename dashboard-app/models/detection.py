from dataclasses import dataclass

@dataclass
class Detection:

    detection_type: str

    severity: str

    details: str
