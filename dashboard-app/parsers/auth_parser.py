import re

log_file = "../logs/auth.log"

with open(log_file, "r") as file:

    logs = file.readlines()

for line in logs:

    if "Failed password" in line:

        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)

        print(f"[ALERT] Failed authentication detected from {ip[0]}")
