import streamlit as st

st.title("Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:
    st.success("Resume Uploaded Successfully!")
    st.write("Filename:", uploaded_file.name)