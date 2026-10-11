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


def extract_skills(text):
    text = str(text).lower()

    found_skills = []

    for skill in IT_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(found_skills)