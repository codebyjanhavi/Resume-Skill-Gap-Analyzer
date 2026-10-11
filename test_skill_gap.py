from resume_parser.pdf_parser import extract_text_from_pdf
from ml.skill_extraction import extract_skills
from ml.skill_gap import calculate_skill_gap


# Resume file
pdf_path = "sample_resume.pdf"


# Extract resume text
resume_text = extract_text_from_pdf(pdf_path)


# Extract candidate skills
candidate_skills = extract_skills(resume_text)


# Job requirements
required_skills = [
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning",
    "TensorFlow",
    "Docker"
]


# Calculate skill gap
result = calculate_skill_gap(
    candidate_skills,
    required_skills
)


print("\nCandidate Skills:")
print(candidate_skills)

print("\nRequired Skills:")
print(required_skills)

print("\nMatched Skills:")
print(result["matched_skills"])

print("\nMissing Skills:")
print(result["missing_skills"])

print("\nExtra Skills:")
print(result["extra_skills"])

print("\nSkill Match Percentage:")
print(result["skill_match_percentage"], "%")