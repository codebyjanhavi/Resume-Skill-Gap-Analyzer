from flask import Flask, render_template, request
import os
import json
from ml.ats_checker import check_ats_readiness
from werkzeug.utils import secure_filename
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
    file = request.files.get("resume")
    selected_role = request.form.get("job_role", "").strip()
    job_description = request.form.get(
        "job_description", ""
    ).strip()

    # Validate uploaded file
    if not file or not file.filename:
        return "Please select a resume."

    filename = secure_filename(file.filename)

    if not filename.lower().endswith((".pdf", ".docx")):
        return "Only PDF and DOCX files are supported."

    if not selected_role and not job_description:
        return (
            "Please select a job role or paste a "
            "job description."
        )

    # Save using a generated filename to avoid collisions
    import uuid

    extension = os.path.splitext(filename)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}{extension}"
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        unique_filename
    )

    file.save(file_path)

    try:
        # Extract resume text
        if extension == ".pdf":
            resume_text = extract_text_from_pdf(file_path)
            ats_result = check_ats_readiness(resume_text)
        else:
            resume_text = extract_text_from_docx(file_path)
            ats_result = check_ats_readiness(resume_text)

        if not resume_text.strip():
            return (
                "No readable text found. If your PDF is "
                "scanned, OCR may be required."
            )

        candidate_skills = extract_skills(resume_text)

        # Use custom job description when provided
        if job_description:
            required_skills = extract_skills(job_description)
            display_role = "Custom Job Description"
        else:
            required_skills = role_skills[selected_role]
            display_role = selected_role

        if not required_skills:
            return (
                "No recognized skills were found in the "
                "job description. Try a predefined role or "
                "include specific technical skills."
            )

        result = calculate_skill_gap(
            candidate_skills,
            required_skills
        )

        recommendations = generate_recommendations(
            result["missing_skills"]
        )

        return render_template(
            "skills.html",
            role=display_role,
            candidate_skills=candidate_skills,
            required_skills=required_skills,
            matched_skills=result["matched_skills"],
            missing_skills=result["missing_skills"],
            extra_skills=result["extra_skills"],
            skill_match_percentage=(
                result["skill_match_percentage"]
            ),
            recommendations=recommendations,
            ats_result=ats_result,
        )

    finally:
        # Remove the temporary uploaded resume
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)