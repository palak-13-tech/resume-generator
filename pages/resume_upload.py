import streamlit as st
import pdfplumber

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    st.session_state["resume_text"] = text

    st.success("Resume Uploaded Successfully!")