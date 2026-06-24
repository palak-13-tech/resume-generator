import streamlit as st
from PyPDF2 import PdfReader

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:
    reader = PdfReader(uploaded_file)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.session_state["resume_text"] = text

    st.success("Resume Uploaded Successfully!")