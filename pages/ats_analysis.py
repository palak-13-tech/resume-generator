import streamlit as st
import re

st.title("ATS Analysis")

resume_text = st.session_state.get("resume_text", "")
jd_text = st.session_state.get("job_description", "")
st.subheader("Resume Preview")
st.write(resume_text[:500])

st.write("Resume Length:", len(resume_text))
st.write("JD Length:", len(jd_text))

if st.button("Calculate ATS Score"):

    if not resume_text:
        st.warning("Please upload resume first")

    elif not jd_text:
        st.warning("Please enter Job Description first")

    else:

        resume_words = set(
            re.findall(r"[a-zA-Z]+", resume_text.lower())
        )

        jd_words = set(
            re.findall(r"[a-zA-Z]+", jd_text.lower())
        )

        matched_skills = resume_words.intersection(jd_words)

        missing_skills = jd_words.difference(resume_words)

        score = round(
            (len(matched_skills) / len(jd_words)) * 100
        )

        st.success(f"ATS Score: {score}%")

        st.progress(score / 100)

        st.subheader("Matched Skills")

        if matched_skills:
            st.success(
                ", ".join(sorted(matched_skills))
            )

        st.subheader("Missing Skills")

        if missing_skills:
            st.warning(
                ", ".join(sorted(missing_skills))
            )