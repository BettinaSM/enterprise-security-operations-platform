# ---------------------------
# RBAC DEFINITIONS
# ---------------------------

ROLE_PERMISSIONS = {

    "admin": [
        "dashboard",
        "detections",
        "incidents",
        "threat_intelligence",
        "compliance",
        "soar",
        "executive"
    ],

    "analyst": [
        "dashboard",
        "detections",
        "incidents",
        "threat_intelligence"
    ],

    "readonly": [
        "dashboard"
    ],

    "manager": [
        "dashboard",
        "executive",
        "compliance"
    ]
}


# ---------------------------
# PERMISSION CHECK
# ---------------------------

def has_permission(
    role,
    permission
):

    permissions = ROLE_PERMISSIONS.get(
        role,
        []
    )

    return permission in permissions
