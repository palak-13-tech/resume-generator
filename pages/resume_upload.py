import streamlit as st

st.title("Resume Upload")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    st.session_state["resume_text"] = uploaded_file.name
    st.success("Resume Uploaded Successfully!")