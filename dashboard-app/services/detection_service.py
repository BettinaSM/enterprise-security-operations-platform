from parsers.detection_engine import (
    run_detections
)

from parsers.yaml_detection_engine import (
    run_yaml_detections
)

from repositories.detections_repository import (
    save_detection_repository
)

def process_detections(events):

    findings = []

    standard = run_detections(events)

    yaml_findings = run_yaml_detections(events)

    findings.extend(standard)
    findings.extend(yaml_findings)

    for detection in findings:

        save_detection_repository(
            detection.get(
                "Detection",
                "Unknown"
            ),
            detection.get(
                "Severity",
                "Medium"
            ),
            str(detection)
        )

    return findings
