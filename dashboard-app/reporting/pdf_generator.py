from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
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

BASE_DIR = Path(__file__).resolve().parent.parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# GENERATE REPORT
# ---------------------------

def generate_security_report(
    detections,
    incidents,
    threat_findings,
    report_type="Security Audit"
):

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{report_type.lower().replace(' ', '_')}_{timestamp}.pdf"
    )

    report_path = REPORT_DIR / filename

    document = SimpleDocTemplate(
        str(report_path),
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ---------------------------
    # COVER
    # ---------------------------

    elements.append(
        Paragraph(
            "Enterprise Security Audit Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 30)
    )

    elements.append(
        Paragraph(
            f"Generated: {datetime.utcnow()} UTC",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Report Type: {report_type}",
            styles["BodyText"]
        )
    )

    elements.append(
        PageBreak()
    )

    # ---------------------------
    # DETECTIONS
    # ---------------------------

    elements.append(
        Paragraph(
            "Detection Findings",
            styles["Heading1"]
        )
    )

    for item in detections[:50]:

        elements.append(
            Paragraph(
                str(item),
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
            "Incident Findings",
            styles["Heading1"]
        )
    )

    for item in incidents[:50]:

        elements.append(
            Paragraph(
                str(item),
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
            "Threat Intelligence Correlation",
            styles["Heading1"]
        )
    )

    for item in threat_findings[:50]:

        elements.append(
            Paragraph(
                str(item),
                styles["BodyText"]
            )
        )

    document.build(elements)

    return report_path
