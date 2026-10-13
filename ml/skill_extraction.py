import re


IT_SKILLS = [
    "API Testing",
    "AWS",
    "Algorithms",
    "Android",
    "Android Studio",
    "Azure",
    "Backup and Recovery",
    "C",
    "C++",
    "CI/CD",
    "CSS",
    "Cloud Security",
    "Communication",
    "Cryptography",
    "Cybersecurity",
    "Data Cleaning",
    "Data Structures",
    "Data Visualization",
    "Database Administration",
    "Database Security",
    "Debugging",
    "Deep Learning",
    "Docker",
    "Documentation",
    "DSA",
    "Ethical Hacking",
    "Excel",
    "Express.js",
    "Firebase",
    "Firewalls",
    "Git",
    "GitHub",
    "HTML",
    "JUnit",
    "Java",
    "JavaScript",
    "Jenkins",
    "Jupyter",
    "Kotlin",
    "Kubernetes",
    "Linux",
    "Machine Learning",
    "Material Design",
    "Matplotlib",
    "MongoDB",
    "Monitoring",
    "MySQL",
    "NLP",
    "Network Security",
    "Networking",
    "Node.js",
    "NumPy",
    "OOP",
    "OWASP",
    "Oracle",
    "Pandas",
    "Performance Tuning",
    "PostgreSQL",
    "Postman",
    "Power BI",
    "Problem Solving",
    "PyTorch",
    "Python",
    "REST API",
    "React",
    "Responsive Design",
    "SIEM",
    "SQL",
    "SQLite",
    "Scikit-learn",
    "Seaborn",
    "Selenium",
    "Shell Scripting",
    "Statistics",
    "Tableau",
    "Team Collaboration",
    "TensorFlow",
    "Test Automation",
    "TestNG",
    "Testing",
    "Transformers",
    "Terraform",
    "Unit Testing",
    "Vulnerability Assessment",
    "XML"
]


SKILL_ALIASES = {
    "js": "JavaScript",
    "javascript": "JavaScript",
    "py": "Python",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "nodejs": "Node.js",
    "reactjs": "React",
    "restful api": "REST API"
}



def extract_skills(text):
    text = str(text).lower()
    found_skills = set()

    # Match the original skill vocabulary
    for skill in IT_SKILLS:
        pattern = r"(?<!\w)" + re.escape(
            skill.lower()
        ) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.add(skill)

    # Match known aliases and normalize them
    for alias, canonical_skill in SKILL_ALIASES.items():
        pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.add(canonical_skill)

    return sorted(found_skills)