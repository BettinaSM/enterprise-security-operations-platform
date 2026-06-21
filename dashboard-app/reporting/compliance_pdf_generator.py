from pathlib import Path

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer

)

from reportlab.lib.styles import (

    getSampleStyleSheet

)

REPORT_DIR = Path(

    "reports"

)

REPORT_DIR.mkdir(

    exist_ok=True

)

# --------------------------------
# GENERATE
# --------------------------------

def generate_compliance_pdf(results):

    report = (

        REPORT_DIR /

        "compliance_report.pdf"

    )

    document = SimpleDocTemplate(

        str(report)

    )

    styles = getSampleStyleSheet()

    story = []

    story.append(

        Paragraph(

            "Compliance Report",

            styles["Title"]

        )

    )

    for key, value in results.items():

        story.append(

            Paragraph(

                f"{key}: {value}%",

                styles["Normal"]

            )

        )

    story.append(

        Spacer(1, 20)

    )

    document.build(story)

    return report
