def generate_incidents():

    return [

        {
            "Incident": "INC-5001",
            "Title": "SSH Brute Force",
            "Priority": "Critical",
            "Owner": "Tier 2",
            "Status": "Investigating",
            "SLA": "15 min",
            "Environment": "Linux"
        },

        {
            "Incident": "INC-5002",
            "Title": "Kubernetes Runtime Alert",
            "Priority": "High",
            "Owner": "Threat Hunting",
            "Status": "Escalated",
            "SLA": "30 min",
            "Environment": "Kubernetes"
        },

        {
            "Incident": "INC-5003",
            "Title": "Suspicious Cloud Login",
            "Priority": "Medium",
            "Owner": "Cloud SOC",
            "Status": "Open",
            "SLA": "1 hour",
            "Environment": "AWS"
        }
    ]
