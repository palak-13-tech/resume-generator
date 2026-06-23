import streamlit as st

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = ""

if "job_description" not in st.session_state:
    st.session_state["job_description"] = ""

st.set_page_config(page_title="AI Resume Pro")

st.title("AI Resume Pro")
st.subheader("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign In"):
    if email and password:
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Enter Email and Password")