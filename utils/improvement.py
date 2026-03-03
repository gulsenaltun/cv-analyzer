def generate_improvements(missing_skills):

    improvements = []

    skill_advice = {
        "python": "Add a Python project demonstrating data processing or automation.",
        "machine learning": "Include an ML project with real datasets and evaluation metrics.",
        "sql": "Show database querying experience or backend development work.",
        "docker": "Containerize one of your projects using Docker.",
        "aws": "Deploy a small application on AWS or another cloud platform.",
        "linux": "Mention Linux usage, terminal commands, or server deployment experience.",
        "git": "Highlight collaborative development using Git and GitHub.",
        "nlp": "Build an NLP project such as text classification or sentiment analysis."
    }

    for skill in missing_skills:
        if skill.lower() in skill_advice:
            improvements.append(skill_advice[skill.lower()])

    if not improvements:
        improvements.append(
            "Your resume already covers most required skills. Focus on measurable achievements."
        )

    return improvements