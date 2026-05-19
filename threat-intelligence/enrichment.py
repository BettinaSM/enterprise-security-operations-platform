ioc_feed = [
    "185.220.101.1",
    "suspicious-runtime.example"
]

event_ip = "185.220.101.1"

if event_ip in ioc_feed:

    print("[ENRICHMENT] Malicious IOC matched")
