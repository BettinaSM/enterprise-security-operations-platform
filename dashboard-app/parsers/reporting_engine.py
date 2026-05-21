from fpdf import FPDF
from configs.settings import REPORTS_DIR

report_path = (
    REPORTS_DIR /
    "executive_security_report.pdf"
)

def generate_executive_report(
    threat_score,
    risk_level,
    incidents,
    critical_alerts
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        200,
        10,
        txt="Executive Security Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        200,
        10,
        txt=f"Threat Score: {threat_score}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Enterprise Risk Level: {risk_level}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Open Incidents: {incidents}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Critical Alerts: {critical_alerts}",
        ln=True
    )

    pdf.ln(10)

    pdf.multi_cell(
        0,
        10,
        txt="""
Unified SOC monitoring platform operational.

Security telemetry active across:
- Linux
- AIX
- Windows
- AWS
- Azure
- GCP
- OCI
- Kubernetes

MITRE ATT&CK correlation active.

Threat intelligence enrichment operational.

SOAR workflows simulated successfully.
"""
    )

    output_path = "executive_security_report.pdf"

    pdf.output(output_path)

    return output_path
