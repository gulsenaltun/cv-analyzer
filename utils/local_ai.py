import requests

def rewrite_cv(cv_text, job_description):

    prompt = f"""
You are an ATS resume optimizer.

Rules:
- Do NOT add fake experience
- Only rewrite existing information
- Optimize for ATS matching

CV:
{cv_text}

JOB DESCRIPTION:
{job_description}

Rewrite the CV professionally.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]