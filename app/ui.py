import streamlit as st


# =====================================================
# SIDEBAR
# =====================================================

def sidebar():

    with st.sidebar:

        st.markdown("# 🤖 AI Recruiter")

        st.markdown("---")

        st.success("🏠 Dashboard")

        st.info("📄 Resume Screening")

        st.info("🎯 Recommendation Engine")

        st.info("📊 Recruiter Analytics")

        st.info("🧠 Skill Gap Analysis")

        st.info("📂 Resume Upload")

        st.info("⬇ Export Results")

        st.markdown("---")

        st.markdown("## ⚙ Tech Stack")

        st.write("✔ Python")

        st.write("✔ NLP")

        st.write("✔ TF-IDF")

        st.write("✔ Cosine Similarity")

        st.write("✔ Machine Learning")

        st.write("✔ Streamlit")

        st.markdown("---")

        st.markdown("### 👩‍💻 Developer")

        st.write("**Trupthi Nazre**")

        st.caption("AI & Data Science")


# =====================================================
# HERO SECTION
# =====================================================

def hero():
    st.markdown(
        """
        <div class="hero">
            <h1>🤖 AI Resume Screening System</h1>
            <p>Intelligent Applicant Tracking System powered by <br><br> NLP • TF-IDF • Machine Learning • AI</p>
        </div>
        """, 
        unsafe_allow_html=True
    )


# =====================================================
# TOP CANDIDATE
# =====================================================

def top_candidate(candidate):

    st.subheader("🏆 Top Candidate")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            label="Category",

            value=candidate["Category"]

        )

    with c2:

        st.metric(

            label="Match Score",

            value=f"{candidate['Match Score']:.2f}%"

        )

    with c3:

        st.metric(

            label="Recommendation",

            value=candidate["Recommendation"]

        )


# =====================================================
# ANALYTICS
# =====================================================

def analytics(results):

    st.subheader("📊 Recruiter Analytics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "📄 Total Resumes",

            len(results)

        )

    with c2:

        st.metric(

            "🏆 Highest Match",

            f"{results['Match Score'].max():.2f}%"

        )

    with c3:

        st.metric(

            "📈 Average Match",

            f"{results['Match Score'].mean():.2f}%"

        )

    with c4:

        st.metric(

            "⭐ Highly Recommended",

            (results["Recommendation"] == "⭐ Highly Recommended").sum()

        )


# =====================================================
# MATCH SCORE CHART
# =====================================================

def match_chart(top10):

    st.subheader("📈 Match Scores")

    chart_data = top10.set_index("Category")["Match Score"]

    st.bar_chart(chart_data)


# =====================================================
# RANKING TABLE
# =====================================================

def ranking_table(top10):

    st.subheader("📋 Resume Rankings")

    st.dataframe(

        top10[
            [
                "Category",
                "Match Score",
                "Recommendation"
            ]
        ],

        use_container_width=True,

        hide_index=True

    )


# =====================================================
# AI INSIGHTS
# =====================================================

def ai_insights(results):

    st.subheader("🤖 AI Recruiter Insights")

    highest = results.iloc[0]["Category"]

    avg = results["Match Score"].mean()

    high = (results["Recommendation"] == "⭐ Highly Recommended").sum()

    if avg >= 25:
        confidence = "High"

    elif avg >= 15:
        confidence = "Medium"

    else:
        confidence = "Low"

    st.info(f"""
### 📌 Hiring Summary

✅ Total resumes analysed : **{len(results)}**

🏆 Best matching category : **{highest}**

📈 Average similarity : **{avg:.2f}%**

⭐ Highly Recommended : **{high}**

🎯 Hiring Confidence : **{confidence}**
""")