import pandas as pd

from src.config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    DRY_RUN
)

from src.logger_setup import setup_logger

from src.template_manager import (
    load_template,
    personalize_template
)

from src.email_sender import send_email

from src.report_generator import generate_report

from src.utils import current_timestamp


# Setup Logger
logger = setup_logger()

print("=" * 60)
print("EMAIL AUTOMATION & REMINDER SYSTEM")
print("=" * 60)


# Load CSV Data
contacts_df = pd.read_csv("data/contacts.csv")

reminders_df = pd.read_csv("data/reminders.csv")


# Load Template
template = load_template(
    "templates/email_template.txt"
)


# Store Report Data
report_data = []


# Process Reminders
for index, reminder in reminders_df.iterrows():

    try:

        # Find Contact
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


        # Prepare Email Data
        email_data = {
            "name": reminder["name"],
            "subject": reminder["subject"],
            "reminder_date": reminder["reminder_date"],
            "department": department
        }


        # Generate Email Body
        email_body = personalize_template(
            template,
            email_data
        )


        # Send Email
        status = send_email(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD,
            receiver_email,
            reminder["subject"],
            email_body,
            DRY_RUN
        )


        # Logging
        logger.info(
            f"{receiver_email} -> {status}"
        )


        # Save Report
        report_data.append({
            "name": reminder["name"],
            "email": receiver_email,
            "subject": reminder["subject"],
            "status": status,
            "timestamp": current_timestamp()
        })


        print(f"Processed: {receiver_email}")


    except Exception as error:

        logger.error(str(error))

        print(f"Error: {error}")


# Generate Final Report
generate_report(report_data)

print("=" * 60)
print("AUTOMATION PROCESS COMPLETED")
print("=" * 60)