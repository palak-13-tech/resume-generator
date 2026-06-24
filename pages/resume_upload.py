import streamlit as st
import pdfplumber

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    st.session_state["resume_text"] = resume_text

    st.success("Resume Uploaded Successfully!")

    st.write("Characters Extracted:", len(resume_text))