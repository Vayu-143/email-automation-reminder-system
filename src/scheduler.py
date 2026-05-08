import schedule
import time

def start_scheduler(job_function):

    schedule.every().day.at(
        "09:00"
    ).do(job_function)

    print("Scheduler started...")

    while True:

        schedule.run_pending()

        time.sleep(1)