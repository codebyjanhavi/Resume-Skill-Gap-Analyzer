
def check_ats_readiness(resume_text):
    """
    Perform a basic ATS-readiness check on resume text.
    Returns a score, suggestions, and detected sections.
    """

    if not resume_text or not resume_text.strip():
        return {
            "score": 0,
            "suggestions": ["Upload a resume containing readable text."],
            "sections": []
        }

    text = resume_text.lower()
    score = 0
    suggestions = []
    sections = []

    # Check resume length
    word_count = len(text.split())

    if word_count >= 150:
        score += 20
    else:
        suggestions.append("Add more relevant details about your skills and experience.")

    # Check common resume sections
    section_keywords = {
        "Contact Information": ["email", "phone", "mobile", "contact"],
        "Education": ["education", "qualification", "degree"],
        "Skills": ["skills", "technical skills", "programming"],
        "Experience": ["experience", "employment", "internship"],
        "Projects": ["projects", "project"]
    }

    for section, keywords in section_keywords.items():
        if any(keyword in text for keyword in keywords):
            sections.append(section)
            score += 16
        else:
            suggestions.append(f"Consider adding a clear {section} section.")

    # Check common formatting-related indicators
    if len(text.splitlines()) >= 10:
        score += 10
    else:
        suggestions.append("Use clear headings and separate sections.")

    score = min(score, 100)

    if not suggestions:
        suggestions.append("Your resume covers the basic checks. Review it for accuracy and relevance.")

    return {
        "score": score,
        "suggestions": suggestions,
        "sections": sections
    }