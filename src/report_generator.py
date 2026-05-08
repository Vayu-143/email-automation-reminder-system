import pandas as pd
import os

def generate_report(report_data):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    report_df = pd.DataFrame(
        report_data
    )

    report_df.to_csv(
        "outputs/report.csv",
        index=False
    )

    print(
        "Report generated successfully!"
    )