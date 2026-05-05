"""
Resume Analyzer — skill gap analysis + career roadmap functions.
Extended for Feature 2 (Skill Gap) and Feature 3 (Career Roadmap).
"""

from data.skills_db import get_required_skills, get_roles

# Comprehensive skills database for basic scoring
skills_db = [
    # Programming Languages
    "python", "java", "c++", "c#", "javascript", "typescript", "go", "rust", "kotlin", "swift",
    # Data & ML
    "machine learning", "data analysis", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch",
    # Databases
    "sql", "nosql", "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
    # Web Technologies
    "html", "css", "react", "vue", "angular", "node", "express", "django", "flask",
    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd", "jenkins",
    # Soft Skills
    "communication", "leadership", "problem solving", "teamwork", "project management",
    "agile", "scrum", "git", "api", "rest", "microservices"
]


def analyze_resume(text):
    """
    Analyze resume text and extract skills.
    Returns tuple of (score, found_skills).
    """
    text = text.lower()
    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    # Calculate score based on found skills (max 100)
    base_score = min(len(found_skills) * 8, 80)

    # Bonus points for specific combinations
    if any(lang in found_skills for lang in ["python", "java", "c++"]):
        base_score = min(base_score + 5, 100)

    if any(ml in found_skills for ml in ["machine learning", "deep learning", "tensorflow"]):
        base_score = min(base_score + 5, 100)

    if any(soft in found_skills for soft in ["communication", "leadership", "teamwork"]):
        base_score = min(base_score + 5, 100)

    score = min(base_score, 100)

    return score, found_skills


def get_skill_gap(user_skills, target_role):
    """
    Compare user skills against target role requirements.

    Returns:
        have: list of skills the user already has
        missing: list of skills the user needs
        match_pct: float (0-100)
    """
    required = get_required_skills(target_role)
    if not required:
        return [], [], 0.0

    user_lower = [s.lower() for s in user_skills]
    have = [s for s in required if s.lower() in user_lower]
    missing = [s for s in required if s.lower() not in user_lower]
    match_pct = (len(have) / len(required)) * 100 if required else 0

    return have, missing, match_pct


# ─── Career Roadmap Data (Feature 3) ─────────────────────────────────

CAREER_PATHS = {
    "software engineer": {
        "path": [
            {"title": "Junior Software Engineer", "years": "0-2", "skills": ["Python/Java", "Git", "SQL", "Testing"]},
            {"title": "Mid-Level Software Engineer", "years": "2-4", "skills": ["System Design", "Docker", "CI/CD", "Code Reviews"]},
            {"title": "Senior Software Engineer", "years": "4-7", "skills": ["Architecture", "Mentoring", "Performance Optimization"]},
            {"title": "Staff / Principal Engineer", "years": "7-10", "skills": ["Tech Strategy", "Cross-team Leadership", "RFC Writing"]},
            {"title": "Engineering Manager / CTO", "years": "10+", "skills": ["People Management", "Budgeting", "Vision Setting"]},
        ],
    },
    "data scientist": {
        "path": [
            {"title": "Junior Data Analyst", "years": "0-1", "skills": ["SQL", "Excel", "Basic Statistics"]},
            {"title": "Data Analyst", "years": "1-3", "skills": ["Python", "Pandas", "Tableau", "A/B Testing"]},
            {"title": "Data Scientist", "years": "3-5", "skills": ["Machine Learning", "Feature Engineering", "Experiment Design"]},
            {"title": "Senior Data Scientist", "years": "5-8", "skills": ["Deep Learning", "MLOps", "Stakeholder Comms"]},
            {"title": "Head of Data / ML Director", "years": "8+", "skills": ["Data Strategy", "Team Building", "Business Alignment"]},
        ],
    },
    "web developer": {
        "path": [
            {"title": "Junior Web Developer", "years": "0-1", "skills": ["HTML/CSS", "JavaScript", "Responsive Design"]},
            {"title": "Frontend Developer", "years": "1-3", "skills": ["React/Vue", "TypeScript", "Testing", "Accessibility"]},
            {"title": "Senior Frontend Engineer", "years": "3-5", "skills": ["Performance", "Architecture", "Design Systems"]},
            {"title": "Full Stack Engineer", "years": "5-7", "skills": ["Node.js", "Databases", "DevOps Basics"]},
            {"title": "Tech Lead / Architect", "years": "7+", "skills": ["System Design", "Team Leadership", "Strategy"]},
        ],
    },
    "frontend engineer": {
        "path": [
            {"title": "Junior Frontend Developer", "years": "0-1", "skills": ["HTML/CSS", "JavaScript Fundamentals"]},
            {"title": "Frontend Developer", "years": "1-3", "skills": ["React", "TypeScript", "Component Libraries"]},
            {"title": "Senior Frontend Engineer", "years": "3-6", "skills": ["Performance", "Accessibility", "Design Systems"]},
            {"title": "Staff Frontend Engineer", "years": "6-9", "skills": ["Architecture", "Micro-frontends", "DX Tooling"]},
            {"title": "Frontend Architect / Director", "years": "9+", "skills": ["Platform Strategy", "Team Building"]},
        ],
    },
    "backend engineer": {
        "path": [
            {"title": "Junior Backend Developer", "years": "0-2", "skills": ["Python/Java", "SQL", "REST APIs"]},
            {"title": "Backend Engineer", "years": "2-4", "skills": ["Docker", "Microservices", "Message Queues"]},
            {"title": "Senior Backend Engineer", "years": "4-7", "skills": ["System Design", "Caching", "Performance"]},
            {"title": "Staff Backend Engineer", "years": "7-10", "skills": ["Distributed Systems", "Tech Roadmapping"]},
            {"title": "Principal Engineer / VP Eng", "years": "10+", "skills": ["Org-wide Architecture", "Strategy"]},
        ],
    },
    "devops engineer": {
        "path": [
            {"title": "Junior SysAdmin / IT Support", "years": "0-1", "skills": ["Linux", "Networking", "Scripting"]},
            {"title": "DevOps Engineer", "years": "1-3", "skills": ["Docker", "CI/CD", "Cloud Basics (AWS/GCP)"]},
            {"title": "Senior DevOps Engineer", "years": "3-5", "skills": ["Kubernetes", "Terraform", "Monitoring"]},
            {"title": "DevOps Architect / SRE Lead", "years": "5-8", "skills": ["Platform Engineering", "SLOs/SLIs", "Cost Optimization"]},
            {"title": "Head of Infrastructure / VP Platform", "years": "8+", "skills": ["Cloud Strategy", "Vendor Management", "Team Building"]},
        ],
    },
    "machine learning engineer": {
        "path": [
            {"title": "ML Intern / Junior Data Scientist", "years": "0-1", "skills": ["Python", "Statistics", "scikit-learn"]},
            {"title": "ML Engineer", "years": "1-3", "skills": ["TensorFlow/PyTorch", "Feature Engineering", "Model Evaluation"]},
            {"title": "Senior ML Engineer", "years": "3-6", "skills": ["MLOps", "Distributed Training", "Production ML"]},
            {"title": "Staff ML Engineer", "years": "6-9", "skills": ["Research", "System Design for ML", "Cross-team Impact"]},
            {"title": "ML Director / AI Lead", "years": "9+", "skills": ["AI Strategy", "Research Direction", "Business Impact"]},
        ],
    },
    "full stack developer": {
        "path": [
            {"title": "Junior Developer", "years": "0-1", "skills": ["HTML/CSS/JS", "Basic Backend"]},
            {"title": "Full Stack Developer", "years": "1-3", "skills": ["React", "Node.js", "SQL", "REST APIs"]},
            {"title": "Senior Full Stack Developer", "years": "3-6", "skills": ["System Design", "DevOps", "Testing"]},
            {"title": "Tech Lead", "years": "6-9", "skills": ["Architecture", "Code Reviews", "Mentoring"]},
            {"title": "Engineering Manager / CTO", "years": "9+", "skills": ["Strategy", "Hiring", "Product Vision"]},
        ],
    },
    "data analyst": {
        "path": [
            {"title": "Junior Data Analyst", "years": "0-1", "skills": ["Excel", "SQL", "Basic Reporting"]},
            {"title": "Data Analyst", "years": "1-3", "skills": ["Python", "Tableau/Power BI", "Statistics"]},
            {"title": "Senior Data Analyst", "years": "3-5", "skills": ["Advanced SQL", "A/B Testing", "Stakeholder Mgmt"]},
            {"title": "Analytics Manager", "years": "5-8", "skills": ["Team Leadership", "Data Strategy"]},
            {"title": "Director of Analytics / CDO", "years": "8+", "skills": ["Org Strategy", "Data Governance"]},
        ],
    },
    "product manager": {
        "path": [
            {"title": "Associate Product Manager", "years": "0-2", "skills": ["User Research", "Wireframing", "Agile"]},
            {"title": "Product Manager", "years": "2-4", "skills": ["Roadmapping", "A/B Testing", "SQL"]},
            {"title": "Senior Product Manager", "years": "4-7", "skills": ["Strategy", "P&L Ownership", "Cross-functional"]},
            {"title": "Director of Product", "years": "7-10", "skills": ["Portfolio Management", "Org Design"]},
            {"title": "VP Product / CPO", "years": "10+", "skills": ["Vision", "Board Communication", "M&A"]},
        ],
    },
    "cloud architect": {
        "path": [
            {"title": "Cloud Support Engineer", "years": "0-2", "skills": ["Linux", "Networking", "One Cloud Provider"]},
            {"title": "Cloud Engineer", "years": "2-4", "skills": ["Multi-cloud", "IaC (Terraform)", "Security"]},
            {"title": "Senior Cloud Engineer", "years": "4-6", "skills": ["Architecture Patterns", "Cost Optimization"]},
            {"title": "Cloud Architect", "years": "6-9", "skills": ["Enterprise Architecture", "Compliance"]},
            {"title": "Chief Architect / VP Cloud", "years": "9+", "skills": ["Strategy", "Vendor Negotiation"]},
        ],
    },
    "cybersecurity analyst": {
        "path": [
            {"title": "IT Security Intern", "years": "0-1", "skills": ["Networking", "Linux", "Basic Security"]},
            {"title": "Security Analyst", "years": "1-3", "skills": ["SIEM", "Incident Response", "Vulnerability Scanning"]},
            {"title": "Senior Security Analyst", "years": "3-6", "skills": ["Pen Testing", "Compliance (SOC2/ISO)"]},
            {"title": "Security Architect", "years": "6-9", "skills": ["Zero Trust", "Security Architecture"]},
            {"title": "CISO / Director of Security", "years": "9+", "skills": ["Risk Management", "Board Reporting"]},
        ],
    },
}


def get_career_roadmap(target_role):
    """
    Get career roadmap for a target role.
    Returns list of milestone dicts or None.
    """
    role_data = CAREER_PATHS.get(target_role.lower())
    if role_data:
        return role_data["path"]
    return None


def detect_current_level(years_of_experience):
    """Estimate current career level from years of experience."""
    if years_of_experience <= 1:
        return "Junior / Entry-Level"
    elif years_of_experience <= 3:
        return "Mid-Level"
    elif years_of_experience <= 6:
        return "Senior"
    elif years_of_experience <= 9:
        return "Staff / Lead"
    else:
        return "Director / Executive"