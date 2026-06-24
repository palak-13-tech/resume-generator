import streamlit as st

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # Temporary store filename as resume text
    st.session_state["resume_text"] = uploaded_file.name

    st.success("Resume Uploaded Successfully!")

    st.write("Filename:", uploaded_file.name)
    st.write("Size:", round(uploaded_file.size/1024, 2), "KB")