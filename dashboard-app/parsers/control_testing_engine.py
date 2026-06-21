from parsers.audit_engine import (
    run_full_audit
)

# --------------------------------
# AUTOMATED CONTROL TESTS
# --------------------------------

def test_account_management():

    audit = run_full_audit()

    users = audit.get(
        "local_users",
        []
    )

    return {

        "control":

            "Account Management",

        "status":

            "PASS"

            if len(users) > 0

            else "FAIL"

    }


def test_sudo_governance():

    audit = run_full_audit()

    sudo = audit.get(
        "sudo_users",
        []
    )

    return {

        "control":

            "Privileged Access",

        "status":

            "PASS"

            if sudo

            else "FAIL"

    }


def execute_control_tests():

    return [

        test_account_management(),

        test_sudo_governance()

    ]
