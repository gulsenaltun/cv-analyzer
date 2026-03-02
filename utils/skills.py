def load_skills():

    with open("data/skills.txt", "r") as f:
        skills = [line.strip().lower() for line in f.readlines()]

    return skills


def extract_skills(text, skills):

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found


def find_missing_skills(cv_skills, job_skills):

    return list(set(job_skills) - set(cv_skills))