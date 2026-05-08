import streamlit as st
import plotly.express as px

from src.analytics import (
    email_statistics
)

from src.database import (
    fetch_reports
)

st.set_page_config(
    page_title="Email Dashboard",
    layout="wide"
)

st.title(
    "📧 Email Automation Dashboard"
)

df = fetch_reports()

if df.empty:

    st.warning(
        "No reports available."
    )

else:

    stats = email_statistics(
        "outputs/report.csv"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Emails",
        stats["total"]
    )

    col2.metric(
        "Success",
        stats["success"]
    )

    col3.metric(
        "Dry Run",
        stats["dry_run"]
    )

    col4.metric(
        "Failed",
        stats["failed"]
    )

    st.subheader("Email Reports")

    st.dataframe(df)

    fig = px.pie(
        names=[
            "Success",
            "Dry Run",
            "Failed"
        ],
        values=[
            stats["success"],
            stats["dry_run"],
            stats["failed"]
        ],
        title="Email Status Analytics"
    )

    st.plotly_chart(fig)