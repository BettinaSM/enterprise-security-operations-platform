from parsers.rbac_engine import (
    has_permission
)

def check_permission(
    role,
    permission
):

    return has_permission(
        role,
        permission
    )
