alerts = [
    "multiple_failed_passwords",
    "shell_execution",
    "privileged_container"
]

if "shell_execution" in alerts and "privileged_container" in alerts:

    print("[CRITICAL] Potential container compromise detected")

elif "multiple_failed_passwords" in alerts:

    print("[HIGH] Potential brute force detected")
