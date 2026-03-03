def generate_feedback(ats_score, missing_skills):

    feedback = []

    if ats_score < 40:
        feedback.append(
            "Your resume is currently not well aligned with this role."
        )

    if len(missing_skills) > 5:
        feedback.append(
            "Several required technical skills are missing."
        )

    if "python" in missing_skills:
        feedback.append(
            "Python proficiency is strongly recommended for this position."
        )

    if "aws" in missing_skills or "docker" in missing_skills:
        feedback.append(
            "Cloud and deployment technologies would significantly improve your profile."
        )

    if not feedback:
        feedback.append(
            "Your resume shows strong alignment with the job requirements."
        )

    return feedback