import sqlite3
import pandas as pd

DATABASE_PATH = "data/automation.db"

def create_database():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS email_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        subject TEXT,
        status TEXT,
        timestamp TEXT
    )
    """)

    connection.commit()
    connection.close()


def insert_report(data):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO email_reports
    (name, email, subject, status, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data["subject"],
        data["status"],
        data["timestamp"]
    ))

    connection.commit()
    connection.close()


def fetch_reports():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    df = pd.read_sql_query(
        "SELECT * FROM email_reports",
        connection
    )

    connection.close()

    return df