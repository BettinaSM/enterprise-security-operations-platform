import random

def generate_realtime_event():

    events = [

        {
            "severity": "Critical",
            "event": "Falco detected container escape"
        },

        {
            "severity": "High",
            "event": "AWS root login detected"
        },

        {
            "severity": "Medium",
            "event": "Multiple failed SSH attempts"
        },

        {
            "severity": "Low",
            "event": "New Kubernetes pod created"
        }
    ]

    return random.choice(events)
