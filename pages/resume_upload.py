import streamlit as st
from PyPDF2 import PdfReader

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    try:
        pdf_reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        st.session_state["resume_text"] = resume_text
        st.write("Characters Extracted:", len(resume_text))
        st.text_area("Resume Preview", resume_text[:1000], height=200)

        st.success("Resume Uploaded Successfully!")

        st.write("Characters Extracted:", len(resume_text))

    except Exception as e:
        st.error(f"Error reading PDF: {e}")