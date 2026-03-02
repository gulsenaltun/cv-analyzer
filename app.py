import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.similarity import calculate_similarity
from utils.skills import load_skills, extract_skills, find_missing_skills

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your CV and paste a job description.")

uploaded_cv = st.file_uploader("Upload CV", type=["pdf"])

if uploaded_cv:
    st.success("CV loaded successfully")

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_cv and job_description:
        with st.spinner("AI is analyzing the documents..."):
            
            cv_text = extract_text_from_pdf(uploaded_cv)
            
            score = calculate_similarity(cv_text, job_description)
            
            skills = load_skills()
            cv_skills = extract_skills(cv_text.lower(), skills) 
            job_skills = extract_skills(job_description.lower(), skills)
            
            missing_skills = find_missing_skills(cv_skills, job_skills)
            
            ats_score = score * 0.7 + (len(cv_skills) / max(len(job_skills), 1)) * 30
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"Semantic Match: {score}%")
            with col2:
                st.subheader(f"ATS Score: {round(ats_score, 2)}%")
            
            if ats_score < 60:
                st.warning("Your CV needs improvement for this role.")
            elif ats_score < 80:
                st.info("Your CV is moderately aligned.")
            else:
                st.success("Strong match for this job!")
                
            st.divider()
            
            st.write("### ✅ Skills in CV")
            st.write(cv_skills)
            
            st.write("### ❌ Missing Skills")
            st.write(missing_skills)
            
    else:
        st.warning("Please upload a CV and paste a job description first.")