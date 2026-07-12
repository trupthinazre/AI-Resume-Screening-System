import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import streamlit as st

from styles import load_css
from ui import (
    sidebar,
    hero,
    top_candidate,
    analytics,
    match_chart,
    ranking_table,
    ai_insights,
)

from utils.screening_engine import screen_resumes


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ======================================================
# LOAD UI
# ======================================================

load_css()

sidebar()

hero()


# ======================================================
# JOB DESCRIPTION
# ======================================================

st.subheader("📋 Enter Job Description")

job_description = st.text_area(
    "",
    height=220,
    placeholder="Paste the complete Job Description here...",
    label_visibility="collapsed",
)


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze = st.button(
        "🚀 Analyze Resumes",
        use_container_width=True,
    )


# ======================================================
# ANALYZE
# ======================================================

if analyze:

    if job_description.strip() == "":

        st.warning("Please enter a Job Description.")

    else:

        with st.spinner("Analyzing resumes..."):

            results = screen_resumes(
                job_description,
                "datasets/resume_dataset.csv",
            )

        st.success("✅ Analysis Completed Successfully!")

        st.divider()

        top_candidate(results.iloc[0])

        st.divider()

        analytics(results)

        st.divider()

        top10 = results.head(10)

        match_chart(top10)

        st.divider()

        ranking_table(top10)

        st.divider()

        ai_insights(results)