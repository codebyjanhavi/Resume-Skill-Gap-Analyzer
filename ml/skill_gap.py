def calculate_skill_gap(candidate_skills, required_skills):

    # Create lowercase lookup sets for case-insensitive comparison
    candidate_lookup = {
        skill.lower(): skill for skill in candidate_skills
    }

    required_lookup = {
        skill.lower(): skill for skill in required_skills
    }

    candidate_set = set(candidate_lookup.keys())
    required_set = set(required_lookup.keys())

    # Find matches and missing skills
    matched_keys = candidate_set.intersection(required_set)
    missing_keys = required_set.difference(candidate_set)
    extra_keys = candidate_set.difference(required_set)

    # Keep original capitalization
    matched_skills = [
        required_lookup[key] for key in matched_keys
    ]

    missing_skills = [
        required_lookup[key] for key in missing_keys
    ]

    extra_skills = [
        candidate_lookup[key] for key in extra_keys
    ]

    # Calculate percentage
    if len(required_set) > 0:
        skill_match_percentage = (
            len(matched_keys) / len(required_set)
        ) * 100
    else:
        skill_match_percentage = 0

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "extra_skills": sorted(extra_skills),
        "skill_match_percentage": round(skill_match_percentage, 2)
    }