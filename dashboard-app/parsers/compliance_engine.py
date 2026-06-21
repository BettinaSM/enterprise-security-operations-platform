import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONTROL_DIR = BASE_DIR / "controls"

# ------------------------------------------------
# LOAD FRAMEWORK
# ------------------------------------------------

def load_framework(filename):

    try:

        with open(
            CONTROL_DIR / filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []

# ------------------------------------------------
# EVALUATE FRAMEWORK
# ------------------------------------------------

def evaluate_framework(

    framework_name,
    controls

):

    implemented = 0

    results = []

    for control in controls:

        status = control.get(

            "implemented",

            False

        )

        if status:

            implemented += 1

        results.append({

            "framework":
                framework_name,

            "control":
                control.get("control"),

            "status":
                "Compliant"
                if status
                else
                "Non-Compliant"

        })

    total = len(controls)

    score = (

        round(
            implemented / total * 100,
            2
        )

        if total > 0
        else 0
    )

    return {

        "framework":
            framework_name,

        "score":
            score,

        "controls":
            results
    }

# ------------------------------------------------
# ENTERPRISE COMPLIANCE
# ------------------------------------------------

def run_compliance():

    frameworks = {

        "NIST":

            load_framework(
                "nist_controls.json"
            ),

        "LGPD":

            load_framework(
                "lgpd_controls.json"
            ),

        "PCI-DSS":

            load_framework(
                "pci_dss_controls.json"
            )

    }

    results = []

    for name, controls in frameworks.items():

        results.append(

            evaluate_framework(
                name,
                controls
            )

        )

    return results

# ------------------------------------------------
# LEGACY COMPATIBILITY
# ------------------------------------------------

def evaluate_controls():

    return run_compliance()
