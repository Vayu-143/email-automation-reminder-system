import pandas as pd

def email_statistics(report_path):

    df = pd.read_csv(report_path)

    total = len(df)

    success = len(
        df[df["status"] == "SUCCESS"]
    )

    dry_run = len(
        df[df["status"] == "DRY_RUN"]
    )

    failed = total - success - dry_run

    return {
        "total": total,
        "success": success,
        "dry_run": dry_run,
        "failed": failed
    }