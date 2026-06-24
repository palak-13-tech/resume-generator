import streamlit as st

st.set_page_config(layout="wide")

st.title("Dashboard")

resume_text = st.session_state.get("resume_text", "")
score = st.session_state.get("ats_score", 0)

col1, col2, col3, col4 = st.columns(4)

with col1:
    uploaded_count = 1 if resume_text else 0
    st.metric("Resume Uploaded", uploaded_count)

with col2:
    st.metric("ATS Score", f"{score}%")

with col3:
    resume_status = "Uploaded" if resume_text else "Not Uploaded"
    st.metric("Resume Status", resume_status)

with col4:
    ats_result = "Ready" if score > 0 else "Pending"
    st.metric("ATS Result", ats_result)

st.divider()

left, right = st.columns([2, 1])

with left:
    st.subheader("ATS Score Overview")
    st.progress(score)
    st.write(f"ATS Score: {score}%")

with right:
    st.subheader("Latest ATS Score")
    st.metric("Current Score", f"{score}%")

st.divider()

if resume_text:
    st.subheader("Resume Preview")
    st.text_area(
        "Resume Content",
        resume_text[:1000],
        height=250
    )