import pandas as pd

from src.config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    DRY_RUN
)

from src.logger_setup import (
    setup_logger
)

from src.template_manager import (
    load_template,
    personalize_template
)

from src.email_sender import (
    send_email
)

from src.report_generator import (
    generate_report
)

from src.utils import (
    current_timestamp
)

from src.database import (
    create_database,
    insert_report
)


# Setup Logger
logger = setup_logger()

# Create Database
create_database()

print("=" * 60)
print("EMAIL AUTOMATION & REMINDER SYSTEM")
print("=" * 60)

# Load CSV Files
contacts_df = pd.read_csv(
    "data/contacts.csv"
)

reminders_df = pd.read_csv(
    "data/reminders.csv"
)

# Load Templates
text_template = load_template(
    "templates/email_template.txt"
)

html_template = load_template(
    "templates/email_template.html"
)

# Report Storage
report_data = []

# Process Reminders
for index, reminder in reminders_df.iterrows():

    try:

        contact = contacts_df[
            contacts_df["name"] == reminder["name"]
        ]

        if contact.empty:

            logger.error(
                f"Contact not found: {reminder['name']}"
            )

            continue

        receiver_email = contact.iloc[0]["email"]

        department = contact.iloc[0]["department"]

        email_data = {
            "name": reminder["name"],
            "subject": reminder["subject"],
            "reminder_date": reminder["reminder_date"],
            "department": department
        }

        # Personalize Text Template
        text_body = personalize_template(
            text_template,
            email_data
        )

        # Personalize HTML Template
        html_body = personalize_template(
            html_template,
            email_data
        )

        # Send Email
        status = send_email(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD,
            receiver_email,
            reminder["subject"],
            text_body,
            html_body,
            DRY_RUN
        )

        # Logging
        logger.info(
            f"{receiver_email} -> {status}"
        )

        # Store Report Data
        report_entry = {
            "name": reminder["name"],
            "email": receiver_email,
            "subject": reminder["subject"],
            "status": status,
            "timestamp": current_timestamp()
        }

        report_data.append(
            report_entry
        )

        # Insert Into SQLite Database
        insert_report(report_entry)

        print(
            f"Processed: {receiver_email}"
        )

    except Exception as error:

        logger.error(
            str(error)
        )

        print(
            f"Error: {error}"
        )

# Generate CSV Report
generate_report(report_data)

print("=" * 60)
print("AUTOMATION PROCESS COMPLETED")
print("=" * 60)