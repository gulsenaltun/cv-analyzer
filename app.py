import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.similarity import calculate_similarity
from utils.skills import load_skills, extract_skills, find_missing_skills
from utils.recommender import generate_recommendations
from utils.feedback import generate_feedback
from utils.improvement import generate_improvements
from utils.local_ai import rewrite_cv
from utils.report import generate_report

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
if "cv_text" not in st.session_state:
    st.session_state.cv_text = None

if "job_description" not in st.session_state:
    st.session_state.job_description = None

if "rewritten_cv" not in st.session_state:
    st.session_state.rewritten_cv = None

st.write("Upload your CV and paste a job description.")

uploaded_cv = st.file_uploader("Upload CV", type=["pdf"])

if uploaded_cv:
    st.success("CV loaded successfully")

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_cv and job_description:
        with st.spinner("AI is analyzing the documents..."):
            
            st.session_state.cv_text = extract_text_from_pdf(uploaded_cv)
            st.session_state.job_description = job_description

            cv_text = st.session_state.cv_text            
            score = calculate_similarity(cv_text, job_description)
            
            skills = load_skills()
            cv_skills = extract_skills(cv_text.lower(), skills) 
            job_skills = extract_skills(job_description.lower(), skills)
            
            missing_skills = find_missing_skills(cv_skills, job_skills)
            recommendations = generate_recommendations(missing_skills)
            
            st.write("### 📊 Skill Match Analysis")

            total_skills = max(len(job_skills), 1)
            skill_match_percent = (len(cv_skills) / total_skills) * 100

            st.progress(int(skill_match_percent))

            st.write(f"Skill Match: {round(skill_match_percent,2)}%")

            st.write("### AI Recommendations")
            for rec in recommendations:
                st.write("👉", rec)
            
            ats_score = score * 0.7 + (len(cv_skills) / max(len(job_skills), 1)) * 30
            feedback = generate_feedback(ats_score, missing_skills)

            report_path = generate_report(
                score,
                round(ats_score,2),
                missing_skills,
                feedback
            )

            with open(report_path, "rb") as f:
                st.download_button(
                    "📄 Download AI Report",
                    f,
                    file_name="AI_Resume_Report.pdf"
                )

            st.write("### 🧑‍💼 Recruiter Feedback")
            improvements = generate_improvements(missing_skills)
            improvements = generate_improvements(missing_skills)

            st.write("###  Recruiter Decision")
            if ats_score > 80:
                st.success("Recommended for Interview ✅")
            elif ats_score > 60:
                st.warning("Consider After Improvements ⚠️")
            else:
                st.error("Not Recommended ❌")

            st.write("### How To Improve Your CV")

            for imp in improvements:
                st.write("👉", imp)

            for f in feedback:
                st.write("✔", f)
            
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

st.divider()

st.subheader("✨ AI CV Optimizer")

if st.button("Rewrite CV for this Job"):

    if st.session_state.cv_text and st.session_state.job_description:

        with st.spinner("AI rewriting your CV..."):

            rewritten = rewrite_cv(
                st.session_state.cv_text,
                st.session_state.job_description
            )

            st.session_state.rewritten_cv = rewritten

    else:
        st.warning("Please analyze resume first.")


if st.session_state.rewritten_cv:
    st.write("### ✨ Optimized CV Version")
    st.write(st.session_state.rewritten_cv)