from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

from pathlib import Path

from datetime import datetime

# ---------------------------
# REPORT DIRECTORY
# ---------------------------

REPORT_DIR = Path(
    "reports"
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# GENERATE PDF REPORT
# ---------------------------

def generate_security_report(
    detections,
    incidents,
    threat_findings
):

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_path = REPORT_DIR / (
        f"soc_report_{timestamp}.pdf"
    )

    document = SimpleDocTemplate(
        str(report_path),
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ---------------------------
    # TITLE
    # ---------------------------

    elements.append(
        Paragraph(
            "Enterprise Security Operations Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ---------------------------
    # DETECTIONS
    # ---------------------------

    elements.append(
        Paragraph(
            "Detections",
            styles["Heading2"]
        )
    )

    for detection in detections[:20]:

        elements.append(
            Paragraph(
                str(detection),
                styles["BodyText"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    # ---------------------------
    # INCIDENTS
    # ---------------------------

    elements.append(
        Paragraph(
            "Incidents",
            styles["Heading2"]
        )
    )

    for incident in incidents[:20]:

        elements.append(
            Paragraph(
                str(incident),
                styles["BodyText"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    # ---------------------------
    # THREAT INTELLIGENCE
    # ---------------------------

    elements.append(
        Paragraph(
            "Threat Intelligence",
            styles["Heading2"]
        )
    )

    for finding in threat_findings[:20]:

        elements.append(
            Paragraph(
                str(finding),
                styles["BodyText"]
            )
        )

    document.build(elements)

    return str(report_path)
