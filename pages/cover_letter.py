import streamlit as st

st.set_page_config(page_title="Cover Letter Generator")

st.title("Cover Letter Generator")
st.write("Generate a professional cover letter for your job application.")

name = st.text_input("Your Name")
job_role = st.text_input("Job Role")
company_name = st.text_input("Company Name")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Cover Letter"):

    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the {job_role} position at {company_name}.

My skills in {skills} make me a strong candidate for this role. I am eager to contribute to your organization and grow professionally.

I have experience working with technical tools and problem-solving approaches that help me adapt quickly and deliver quality results. I am enthusiastic about learning new technologies and contributing effectively to your team.

Thank you for your consideration. I look forward to the opportunity to discuss how my skills and qualifications align with your requirements.

Sincerely,

{name}
"""

    st.text_area(
        "Generated Cover Letter",
        cover_letter,
        height=350
    )

    st.download_button(
        label="📄 Download Cover Letter",
        data=cover_letter,
        file_name="cover_letter.txt",
        mime="text/plain"
    )