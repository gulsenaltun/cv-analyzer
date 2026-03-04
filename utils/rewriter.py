from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_cv(cv_text, job_description):

    prompt = f"""
You are an ATS resume optimizer.

Rules:
- NEVER add fake experience
- NEVER invent skills
- ONLY rephrase existing sentences
- Optimize wording for ATS matching

CV:
{cv_text}

JOB DESCRIPTION:
{job_description}

Rewrite the CV professionally.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content