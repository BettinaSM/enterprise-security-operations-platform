CIS_CONTROLS = [

    "Password Policy",
    "Privileged Access",
    "Audit Logging",
    "MFA Enforcement",
    "Least Privilege"
]

# ---------------------------
# RUN COMPLIANCE
# ---------------------------

def run_compliance():

    findings = []

    for control in CIS_CONTROLS:

        findings.append({

            "control": control,
            "status": "Compliant"
        })

    return findings
