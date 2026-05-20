import random

def generate_live_metrics():

    return {

        "critical_alerts": random.randint(1, 20),

        "runtime_threats": random.randint(5, 40),

        "failed_auth": random.randint(10, 100),

        "incidents": random.randint(1, 15)
    }
