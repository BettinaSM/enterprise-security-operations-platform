from services.reporting_service import generate_daily_report

from services.audit_service import execute_enterprise_audit

from services.baseline_service import create_baseline

from utils.logger import log_info


def run_daily_audit():

    log_info(
        "Running daily audit"
    )

    execute_enterprise_audit()


def run_daily_reports():

    log_info(
        "Generating executive reports"
    )

    generate_daily_report()


def run_baseline_job():

    log_info(
        "Running baseline verification"
    )

    create_baseline(
        "daily_baseline",
        "enterprise"
    )
