import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

DRY_RUN = os.getenv(
    "DRY_RUN",
    "True"
) == "True"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465