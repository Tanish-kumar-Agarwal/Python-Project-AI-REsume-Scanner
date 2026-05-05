"""
Job Recommender — job matching + skill gap detection.
Extended with mock SKILLS_DB integration.
"""

from data.skills_db import SKILLS_DB, get_required_skills

# Comprehensive job database with required skills
jobs_db = [
    {"title": "Software Engineer", "skills": ["python", "java", "c++", "sql", "git", "api"], "level": "Mid-Level"},
    {"title": "Data Scientist", "skills": ["python", "machine learning", "sql", "data analysis", "tensorflow"], "level": "Mid-Level"},
    {"title": "Web Developer", "skills": ["html", "css", "javascript", "react", "node"], "level": "Junior"},
    {"title": "DevOps Engineer", "skills": ["docker", "kubernetes", "aws", "ci/cd", "git"], "level": "Mid-Level"},
    {"title": "Backend Engineer", "skills": ["python", "java", "sql", "api", "microservices"], "level": "Mid-Level"},
    {"title": "Frontend Engineer", "skills": ["javascript", "react", "html", "css", "typescript"], "level": "Junior"},
    {"title": "Machine Learning Engineer", "skills": ["python", "machine learning", "deep learning", "tensorflow", "data analysis"], "level": "Senior"},
    {"title": "Full Stack Developer", "skills": ["javascript", "python", "react", "node", "sql"], "level": "Mid-Level"},
    {"title": "Data Analyst", "skills": ["sql", "python", "excel", "data visualization", "statistics"], "level": "Junior"},
    {"title": "Product Manager", "skills": ["agile", "communication", "data analysis", "leadership", "project management"], "level": "Mid-Level"},
    {"title": "Cloud Architect", "skills": ["aws", "azure", "docker", "kubernetes", "terraform"], "level": "Senior"},
    {"title": "Cybersecurity Analyst", "skills": ["networking", "linux", "security", "python", "scripting"], "level": "Mid-Level"},
]


def recommend_jobs(user_skills):
    """
    Recommend jobs based on user skills.
    Returns list of tuples (job_title, match_percentage).
    """
    recommendations = []

    for job in jobs_db:
        match_count = len(set(user_skills) & set(job["skills"]))
        score = int((match_count / len(job["skills"])) * 100)

        recommendations.append((job["title"], score))

    # Sort by score in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations


def get_job_details(job_title):
    """
    Get detailed information about a specific job.
    """
    for job in jobs_db:
        if job["title"].lower() == job_title.lower():
            return job
    return None


def get_missing_skills(user_skills, job_title):
    """
    Get skills missing for a specific job.
    Uses SKILLS_DB for comprehensive matching if available,
    falls back to jobs_db.
    """
    # Try SKILLS_DB first (more comprehensive)
    required = get_required_skills(job_title)
    if required:
        user_lower = [s.lower() for s in user_skills]
        missing = [s for s in required if s.lower() not in user_lower]
        return missing

    # Fallback to jobs_db
    job = get_job_details(job_title)
    if job:
        missing = [s for s in job["skills"] if s not in user_skills]
        return missing
    return []


def get_matching_skills(user_skills, job_title):
    """
    Get skills the user has that match a specific job.
    """
    required = get_required_skills(job_title)
    if required:
        user_lower = [s.lower() for s in user_skills]
        matching = [s for s in required if s.lower() in user_lower]
        return matching

    job = get_job_details(job_title)
    if job:
        matching = [s for s in job["skills"] if s in user_skills]
        return matching
    return []