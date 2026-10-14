
import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "datasets" / "resume_match_dataset.csv"
MODEL_PATH = ROOT / "ml" / "resume_match_model.joblib"

# Load the labeled dataset
df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=["resume_text", "job_description", "label"])
df["label"] = df["label"].astype(int)

# Combine resume and job-description text into one input
X = (
    "RESUME: " + df["resume_text"].astype(str)
    + " JOB: " + df["job_description"].astype(str)
)
y = df["label"]

if y.nunique() < 2:
    raise ValueError("Dataset must contain both label 0 and label 1.")

# Keep some examples aside for testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Convert text to TF-IDF features and train the classifier
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

# Evaluate on unseen test examples
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, zero_division=0))

# Save the complete pipeline
joblib.dump(model, MODEL_PATH)
print(f"Model saved to: {MODEL_PATH}")
