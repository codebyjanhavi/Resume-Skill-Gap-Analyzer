
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "ml" / "resume_match_model.joblib"

# Load the trained model
model = joblib.load(MODEL_PATH)


def predict_resume_match(resume_text, job_description):
    combined_text = (
        f"RESUME: {resume_text} "
        f"JOB: {job_description}"
    )

    prediction = int(model.predict([combined_text])[0])

    probabilities = model.predict_proba([combined_text])[0]
    classes = list(model.classes_)

    match_probability = float(
        probabilities[classes.index(1)]
    ) * 100

    return {
        "prediction": (
            "Match" if prediction == 1 else "Not a Match"
        ),
        "match_probability": round(match_probability, 2)
    }
