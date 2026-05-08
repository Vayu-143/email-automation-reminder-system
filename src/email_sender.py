import smtplib

from email.message import EmailMessage


def send_email(
    sender_email,
    password,
    receiver_email,
    subject,
    text_body,
    html_body=None,
    dry_run=True
):

    if dry_run:

        print(
            f"[DRY RUN] Email simulated for {receiver_email}"
        )

        return "DRY_RUN"

    try:

        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(text_body)

        if html_body:

            msg.add_alternative(
                html_body,
                subtype="html"
            )

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                sender_email,
                password
            )

            smtp.send_message(msg)

        print(
            f"Email sent to {receiver_email}"
        )

        return "SUCCESS"

    except Exception as error:

        print(error)

        return f"FAILED: {error}"