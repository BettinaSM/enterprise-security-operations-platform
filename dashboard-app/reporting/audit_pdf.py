from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from pathlib import Path
from datetime import datetime

REPORT_DIR = (
    Path(__file__).resolve().parent.parent /
    "reports"
)

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ---------------------------
# GENERATE AUDIT PDF
# ---------------------------

def generate_audit_pdf(
    title,
    content
):

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    pdf_path = (
        REPORT_DIR /
        f"audit_report_{timestamp}.pdf"
    )

    document = SimpleDocTemplate(
        str(pdf_path)
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            title,
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    document.build(
        elements
    )

    return pdf_path
