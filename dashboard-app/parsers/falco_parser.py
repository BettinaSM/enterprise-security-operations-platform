log_file = "../logs/falco-events.log"

with open(log_file, "r") as file:

    logs = file.readlines()

for line in logs:

    if "Critical" in line:
        print("[HIGH] Runtime security incident detected")

    elif "Warning" in line:
        print("[MEDIUM] Suspicious runtime activity")
