import streamlit as st

st.title("Cover Letter Generator")

name = st.text_input("Your Name")
job_role = st.text_input("Job Role")
company_name = st.text_input("Company Name")
skills = st.text_area("Skills")

if st.button("Generate Cover Letter"):

    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the {job_role} position at {company_name}.

My skills in {skills} make me a strong candidate for this role. I am eager to contribute to your organization and grow professionally.

Thank you for your consideration.

Sincerely,
{name}
"""

    st.text_area("Generated Cover Letter", cover_letter, height=300)