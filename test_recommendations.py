from ml.recommendations import generate_recommendations



missing_skills = [
    "Docker",
    "PyTorch",
    "REST API",
    "Scikit-learn"
]


recommendations = generate_recommendations(missing_skills)


print("Skill Gap Recommendations:")

for item in recommendations:
    print("\nSkill:", item["skill"])
    print("Recommendation:", item["recommendation"])