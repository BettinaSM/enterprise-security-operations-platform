from pathlib import Path

from parsers.cmdb_engine import (
    load_cmdb
)

# ---------------------------
# DATABASE
# ---------------------------

def check_database():

    try:

        from database.database import engine

        connection = engine.connect()

        connection.close()

        return "Healthy"

    except:

        return "Unhealthy"


# ---------------------------
# CMDB
# ---------------------------

def check_cmdb():

    try:

        assets = load_cmdb()

        return (

            "Healthy"

            if assets

            else "Empty"

        )

    except:

        return "Unhealthy"


# ---------------------------
# THREAT FEED
# ---------------------------

def check_threat_feed():

    try:

        path = (

            Path(__file__).resolve()

            .parent.parent /

            "threat-intelligence" /

            "threat-feed.json"

        )

        return (

            "Healthy"

            if path.exists()

            else "Missing"

        )

    except:

        return "Unhealthy"


# ---------------------------
# REPORTS
# ---------------------------

def check_reports():

    try:

        path = (

            Path(__file__).resolve()

            .parent.parent /

            "reports"

        )

        return (

            "Healthy"

            if path.exists()

            else "Missing"

        )

    except:

        return "Unhealthy"


# ---------------------------
# BASELINES
# ---------------------------

def check_baselines():

    try:

        path = (

            Path(__file__).resolve()

            .parent.parent /

            "baseline"

        )

        return (

            "Healthy"

            if path.exists()

            else "Missing"

        )

    except:

        return "Unhealthy"


# ---------------------------
# PLATFORM
# ---------------------------

def run_platform_health():

    return [

        {

            "Service": "Database",

            "Status":

                check_database()

        },

        {

            "Service": "CMDB",

            "Status":

                check_cmdb()

        },

        {

            "Service": "Threat Intelligence",

            "Status":

                check_threat_feed()

        },

        {

            "Service": "Reports",

            "Status":

                check_reports()

        },

        {

            "Service": "Baseline Repository",

            "Status":

                check_baselines()

        }

    ]
