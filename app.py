from flask import Flask, render_template, request
import os
import json
from resume_parser.pdf_parser import extract_text_from_pdf
from resume_parser.docx_parser import extract_text_from_docx

from ml.skill_extraction import extract_skills
from ml.skill_gap import calculate_skill_gap
from ml.recommendations import generate_recommendations


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Load role skill profiles
with open("data/role_skills.json", "r") as file:
    role_skills = json.load(file)


@app.route("/")
def home():

    roles = sorted(role_skills.keys())

    return render_template(
        "upload.html",
        roles=roles
    )



@app.route("/upload", methods=["POST"])
def upload_resume():

    file = request.files["resume"]
    selected_role = request.form.get("job_role")

    if file.filename == "":
        return "No file selected"

    if not selected_role:
        return "Please select a job role"

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)

    # Extract resume text
    if file.filename.lower().endswith(".pdf"):

        resume_text = extract_text_from_pdf(file_path)

    elif file.filename.lower().endswith(".docx"):

        resume_text = extract_text_from_docx(file_path)

    else:

        return "Only PDF and DOCX files are supported"

    # Extract candidate skills
    candidate_skills = extract_skills(resume_text)

    # Get required skills for selected role
    required_skills = role_skills[selected_role]

    # Calculate skill gap
    result = calculate_skill_gap(
        candidate_skills,
        required_skills
    )

    recommendations = generate_recommendations(
        result["missing_skills"]
    )

    return render_template(
        "skills.html",
        role=selected_role,
        candidate_skills=candidate_skills,
        required_skills=required_skills,
        matched_skills=result["matched_skills"],
        missing_skills=result["missing_skills"],
        extra_skills=result["extra_skills"],
        skill_match_percentage=result["skill_match_percentage"],
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)