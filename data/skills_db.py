"""
Mock skills database: {job_role: [required_skills]}
Used by Feature 2 (Skill Gap) and Feature 7 (ATS Score).
"""

SKILLS_DB = {
    "software engineer": [
        "python", "java", "c++", "sql", "git", "api", "rest",
        "data structures", "algorithms", "problem solving",
        "docker", "linux", "testing", "agile", "communication"
    ],
    "data scientist": [
        "python", "sql", "machine learning", "data analysis",
        "tensorflow", "pytorch", "statistics", "pandas", "numpy",
        "data visualization", "r", "deep learning", "nlp",
        "communication", "problem solving"
    ],
    "web developer": [
        "javascript", "html", "css", "react", "node", "typescript",
        "api", "rest", "git", "responsive design", "testing",
        "webpack", "agile", "communication", "problem solving"
    ],
    "frontend engineer": [
        "javascript", "react", "html", "css", "typescript",
        "responsive design", "webpack", "testing", "git",
        "ui/ux", "accessibility", "performance optimization",
        "agile", "communication", "problem solving"
    ],
    "backend engineer": [
        "python", "java", "sql", "api", "rest", "microservices",
        "docker", "kubernetes", "redis", "postgresql", "mongodb",
        "git", "linux", "testing", "agile"
    ],
    "devops engineer": [
        "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd",
        "jenkins", "terraform", "ansible", "linux", "git",
        "monitoring", "networking", "scripting", "python"
    ],
    "machine learning engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "data analysis", "sql", "docker", "kubernetes",
        "mlops", "statistics", "computer vision", "nlp",
        "git", "problem solving"
    ],
    "full stack developer": [
        "javascript", "python", "react", "node", "sql", "html",
        "css", "api", "rest", "git", "docker", "mongodb",
        "typescript", "testing", "agile"
    ],
    "data analyst": [
        "sql", "python", "excel", "data visualization", "tableau",
        "power bi", "statistics", "pandas", "numpy", "r",
        "communication", "problem solving", "data analysis",
        "reporting", "etl"
    ],
    "product manager": [
        "agile", "scrum", "communication", "leadership",
        "problem solving", "data analysis", "sql", "project management",
        "wireframing", "a/b testing", "user research",
        "roadmap planning", "stakeholder management",
        "market research", "strategy"
    ],
    "cloud architect": [
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
        "networking", "security", "microservices", "linux",
        "ci/cd", "monitoring", "python", "cost optimization",
        "architecture design"
    ],
    "cybersecurity analyst": [
        "networking", "linux", "python", "security", "firewalls",
        "penetration testing", "siem", "incident response",
        "vulnerability assessment", "encryption", "compliance",
        "risk management", "communication", "problem solving",
        "scripting"
    ],
}


def get_roles():
    """Return sorted list of all available job roles."""
    return sorted(SKILLS_DB.keys())


def get_required_skills(role):
    """Return required skills for a given role (case-insensitive)."""
    return SKILLS_DB.get(role.lower(), [])
