import streamlit as st

st.set_page_config(layout="wide")

st.title("Dashboard")
resume_text = st.session_state.get("resume_text", "")
score = st.session_state.get("ats_score", 0)

# Top Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
   if resume_text:
        uploaded_count = 1
   else:
        uploaded_count = 0

        st.metric("Resume Uploaded", uploaded_count) 

with col2:
    score = st.session_state.get("ats_score", 0)

    st.metric("ATS Score", f"{score}%")

with col3:
    if resume_text:
        resume_status = "Uploaded"
    else:
        resume_status = "Not Uploaded"

    st.metric("Resume Status", resume_status)

with col4:
    if score > 0:
      ats_result = "Ready"
    else:
      ats_result = "Pending"

st.metric("ATS Result", ats_result)

st.divider()

# Charts Section
left, right = st.columns([2, 1])

with left:
    st.subheader("ATS Score Overview")

    score = st.session_state.get("ats_score", 0)
    st.progress(score)
    st.write(f"ATS Score: {score}%")

    
with right:
    st.subheader("Latest ATS Score")
    score = st.session_state.get("ats_score", 0)
    st.metric("Current Score", f"{score}%")

st.divider()

