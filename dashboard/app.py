import sys
import os

# Fix Streamlit deployment import issue
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import plotly.express as px

from src.analytics import (
    email_statistics
)

from src.database import (
    fetch_reports
)

# Streamlit Page Configuration
st.set_page_config(
    page_title="Email Dashboard",
    layout="wide"
)

# Dashboard Title
st.title(
    "📧 Email Automation Dashboard"
)

# Fetch Database Reports
df = fetch_reports()

# If No Data
if df.empty:

    st.warning(
        "No reports available."
    )

else:

    # Analytics Statistics
    stats = email_statistics(
        "outputs/report.csv"
    )

    # Metrics Row
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

    # Reports Table
    st.subheader(
        "Email Reports"
    )

    st.dataframe(df)

    # Pie Chart Analytics
    st.subheader(
        "Email Status Analytics"
    )

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
        title="Email Status Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Footer
st.markdown("---")

st.markdown(
    "Developed using Python, Streamlit, SQLite, Pandas, and Plotly 🚀"
)