def generate_recommendations(missing_skills):

    recommendations = []

    skill_advice = {
        "docker": "Learn Docker to improve deployment and DevOps skills.",
        "aws": "Learning AWS will strengthen your cloud engineering profile.",
        "react": "React knowledge improves frontend compatibility.",
        "machine learning": "Deepen ML knowledge with real-world projects.",
        "sql": "Advanced SQL improves data handling capabilities.",
        "git": "Strong Git usage shows team collaboration skills.",
        "linux": "Linux knowledge is valuable for backend environments."
    }

    for skill in missing_skills:
        if skill in skill_advice:
            recommendations.append(skill_advice[skill])
        else:
            recommendations.append(f"Consider learning {skill} to improve job compatibility.")

    return recommendations