import streamlit as st
import re

st.title("ATS Analysis")

# Show stored data lengths
st.write("Resume Length:", len(st.session_state.get("resume_text", "")))
st.write("JD Length:", len(st.session_state.get("job_description", "")))

if st.button("Calculate ATS Score"):

    resume_text = st.session_state.get("resume_text", "")
    jd_text = st.session_state.get("job_description", "")

    if resume_text == "" or jd_text == "":
        st.warning("Upload Resume and Save Job Description First")

    else:

        # Extract words properly
        resume_words = set(re.findall(r"\w+", resume_text.lower()))
        jd_words = set(re.findall(r"\w+", jd_text.lower()))

        # Matching and missing skills
        matched_skills = resume_words & jd_words
        missing_skills = jd_words - resume_words

        # ATS Score
        score = int((len(matched_skills) / len(jd_words)) * 100)
        st.session_state["ats_score"] = score
        # Display score
        st.success(f"ATS Score: {score}%")

        # Progress bar
        st.progress(score / 100)

        # Matched Skills
        st.subheader("Matched Skills")

        if matched_skills:
            st.success(", ".join(sorted(matched_skills)))
        else:
            st.error("No matching skills found")

        # Missing Skills
        st.subheader("Missing Skills")

        if missing_skills:
            st.warning(", ".join(sorted(missing_skills)))
        else:
            st.success("No missing skills")