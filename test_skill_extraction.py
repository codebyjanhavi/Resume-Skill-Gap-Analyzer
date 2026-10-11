from resume_parser.pdf_parser import extract_text_from_pdf
from ml.skill_extraction import extract_skills


pdf_path = "sample_resume.pdf"

# Extract resume text
resume_text = extract_text_from_pdf(pdf_path)

# Extract skills
skills = extract_skills(resume_text)

print("Detected Skills:")
print(skills)