import pandas as pd
import json

df = pd.read_csv("data/resume_skill_gap_dataset_v2.csv")

role_skills = {}

for role in df["job_role"].unique():

    role_data = df[df["job_role"] == role]

    skill_count = {}

    for skill_list in role_data["skills"]:

        skills = set(skill.strip() for skill in skill_list.split(","))

        for skill in skills:
            skill_count[skill] = skill_count.get(skill, 0) + 1

    total_resumes = len(role_data)

    common_skills = []

    for skill, count in skill_count.items():

        frequency = count / total_resumes

        if frequency >= 0.50:
            common_skills.append(skill)

    role_skills[role] = sorted(common_skills)


# Save role skills to JSON file
with open("data/role_skills.json", "w") as file:
    json.dump(role_skills, file, indent=4)


# Display the role skills
for role, skills in role_skills.items():

    print("\n" + role)
    print(skills)

print("\nRole skill profiles saved successfully!")