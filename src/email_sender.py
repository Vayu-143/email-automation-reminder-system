import smtplib
from email.message import EmailMessage

def send_email(
    sender_email,
    password,
    receiver_email,
    subject,
    body,
    dry_run=True
):

    if dry_run:
        print(f"[DRY RUN] Email simulated for {receiver_email}")
        return "DRY_RUN"

    try:

        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(sender_email, password)
            smtp.send_message(msg)

        print(f"Email sent successfully to {receiver_email}")

        return "SUCCESS"

    except Exception as error:

        print(f"Failed to send email to {receiver_email}")

        return f"FAILED: {error}"