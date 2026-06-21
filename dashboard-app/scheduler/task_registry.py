from scheduler.jobs import *

TASKS = {

    "daily_audit":
        run_daily_audit,

    "daily_report":
        run_daily_reports,

    "baseline":
        run_baseline_job
}
