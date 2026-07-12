def compare_skills(resume_skills, jd_skills):
    """
    Compare resume skills with job description skills.
    """

    matched_skills = sorted(set(resume_skills) & set(jd_skills))

    missing_skills = sorted(set(jd_skills) - set(resume_skills))

    return matched_skills, missing_skills
