from apscheduler.schedulers.background import (

    BackgroundScheduler

)

from scheduler.task_registry import TASKS

scheduler = BackgroundScheduler()

scheduler.add_job(

    TASKS["daily_audit"],

    "cron",

    hour=1

)

scheduler.add_job(

    TASKS["daily_report"],

    "cron",

    hour=6

)

scheduler.add_job(

    TASKS["baseline"],

    "interval",

    hours=12

)

scheduler.start()
