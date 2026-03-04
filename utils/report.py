from fpdf import FPDF

def generate_report(score, ats_score, missing_skills, feedback):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,"AI Resume Analysis Report", ln=True)

    pdf.cell(200,10,f"Semantic Match: {score}%", ln=True)
    pdf.cell(200,10,f"ATS Score: {ats_score}%", ln=True)

    pdf.cell(200,10,"Missing Skills:", ln=True)

    for skill in missing_skills:
        pdf.cell(200,10,f"- {skill}", ln=True)

    pdf.cell(200,10,"Feedback:", ln=True)

    for f in feedback:
        pdf.cell(200,10,f"- {f}", ln=True)

    path = "report.pdf"
    pdf.output(path)

    return path