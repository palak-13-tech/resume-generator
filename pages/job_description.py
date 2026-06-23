import streamlit as st
import data

st.title("Job Description")

jd = st.text_area(
    "Paste Job Description Here",
    height=300
)

if st.button("Save Job Description"):
    st.session_state["job_description"] = jd
    st.success("Job Description Saved Successfully")