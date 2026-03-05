# AI Resume Analyzer

An AI-powered resume analysis tool that evaluates how well a CV matches a job description.

The system performs semantic analysis, skill gap detection, and ATS scoring while providing AI-based improvement suggestions.

## Features

- CV parsing from PDF
- Semantic similarity analysis
- ATS compatibility scoring
- Skill gap detection
- Recruiter-style feedback
- AI-generated CV improvements
- Local LLM integration using Llama3 (Ollama)

## Tech Stack

Python  
Streamlit  
Scikit-learn  
TF-IDF & Cosine Similarity  
Local LLM (Llama3 via Ollama)

## How It Works

1. Upload your CV in PDF format
2. Paste a job description
3. The system analyzes:
   - Semantic match
   - Skill overlap
   - ATS score
4. AI suggests improvements and rewrites your CV.

## Run Locally

```bash
git clone https://github.com/gulsenaltun/cv-analyzer.git
cd cv-analyzer
pip install -r requirements.txt
streamlit run app.py



