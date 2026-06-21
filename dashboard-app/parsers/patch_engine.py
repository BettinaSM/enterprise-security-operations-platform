from parsers.vulnerability_engine import (
    enrich_vulnerabilities
)

# --------------------------------
# PATCH RECOMMENDATIONS
# --------------------------------

def recommend_patching():

    recommendations = []

    vulns = enrich_vulnerabilities()

    for vuln in vulns:

        if vuln["severity"] in [

            "Critical",
            "High"

        ]:

            recommendations.append({

                "hostname":
                    vuln["hostname"],

                "package":
                    vuln.get(
                        "package",
                        "Unknown"
                    ),

                "cve":
                    vuln["cve"],

                "action":
                    "Immediate patch required"

            })

    return recommendations
