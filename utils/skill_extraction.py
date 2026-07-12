# List of predefined technical skills

SKILLS = {

    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle",

    # Data Science
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "statistics",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",

    # AI
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "nlp",

    # Big Data
    "hadoop",
    "spark",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",

    # Visualization
    "power bi",
    "tableau",
    "excel",

    # Web Development
    "html",
    "css",
    "react",
    "nodejs",
    "flask",
    "django",

    # Soft Skills
    "communication",
    "problem solving",

    # Operating System
    "linux"
}


def extract_skills(text):
    """
    Extract predefined technical skills from text.
    """

    text = text.lower()

    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return sorted(found_skills)