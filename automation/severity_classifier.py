alerts = [
    "Failed password",
    "Shell spawned inside container",
    "Privilege escalation"
]

for alert in alerts:

    if "Privilege" in alert:
        print(f"{alert} -> CRITICAL")

    elif "Shell" in alert:
        print(f"{alert} -> HIGH")

    else:
        print(f"{alert} -> MEDIUM")
