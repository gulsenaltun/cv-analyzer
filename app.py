import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.similarity import calculate_similarity
from utils.skills import load_skills, extract_skills, find_missing_skills


st.set_page_config(page_title="AI CV Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your CV and paste a job description to see analysis.")

uploaded_cv = st.file_uploader(
    "Upload your CV (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)


if uploaded_cv and job_description:

    # CV TEXT
    cv_text = extract_text_from_pdf(uploaded_cv)

    # SIMILARITY SCORE
    score = calculate_similarity(cv_text, job_description)

    st.subheader(f"Match Score: {score}%")

    # SKILL ANALYSIS
    skills = load_skills()

    cv_skills = extract_skills(cv_text, skills)
    job_skills = extract_skills(job_description.lower(), skills)

    missing_skills = find_missing_skills(cv_skills, job_skills)

    st.write("### ✅ Skills Found in CV")
    st.write(cv_skills)

    st.write("### ❌ Missing Skills")
    st.write(missing_skills)