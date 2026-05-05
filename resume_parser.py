"""
Resume Parser — PDF text extraction + regex-based field extraction.
This is the load-bearing module: every other feature reads from its output.
"""

import re
import fitz  # PyMuPDF


def extract_text_from_pdf(file_path):
    """Extract raw text from a PDF file using PyMuPDF."""
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text


def extract_text_from_bytes(file_bytes):
    """Extract raw text from PDF bytes (for st.file_uploader)."""
    text = ""
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text


def parse_resume(text):
    """
    Parse resume text using regex to extract structured fields.

    Returns dict:
        - name (str)
        - email (str)
        - phone (str)
        - skills (list[str])
        - education (list[str])
        - years_of_experience (int)
        - raw_text (str)
    """
    result = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": [],
        "education": [],
        "years_of_experience": 0,
        "raw_text": text,
    }

    # --- EMAIL ---
    email_pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    email_match = re.search(email_pattern, text)
    if email_match:
        result["email"] = email_match.group()

    # --- PHONE ---
    phone_pattern = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        result["phone"] = phone_match.group().strip()

    # --- NAME (first non-empty line, heuristic) ---
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if lines:
        # Name is usually the first line that isn't an email/phone/URL
        for line in lines[:5]:
            if not re.search(email_pattern, line) and not re.search(phone_pattern, line) and not line.startswith("http"):
                # Likely a name if it's short and mostly alphabetic
                if len(line) < 60 and re.match(r'^[A-Za-z\s.\-,]+$', line):
                    result["name"] = line
                    break

    # --- SKILLS ---
    skills_db = [
        "python", "java", "c++", "c#", "javascript", "typescript", "go", "rust",
        "kotlin", "swift", "ruby", "php", "scala", "r",
        "machine learning", "data analysis", "deep learning", "nlp",
        "computer vision", "tensorflow", "pytorch", "keras",
        "sql", "nosql", "mongodb", "postgresql", "mysql", "redis",
        "elasticsearch", "dynamodb",
        "html", "css", "react", "vue", "angular", "svelte", "next.js",
        "node", "express", "django", "flask", "fastapi", "spring",
        "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd", "jenkins",
        "terraform", "ansible", "github actions",
        "git", "linux", "api", "rest", "graphql", "grpc", "microservices",
        "agile", "scrum", "jira",
        "pandas", "numpy", "matplotlib", "scikit-learn", "spark", "hadoop",
        "tableau", "power bi", "excel",
        "communication", "leadership", "problem solving", "teamwork",
        "project management", "critical thinking",
        "testing", "selenium", "cypress", "jest", "pytest",
        "figma", "sketch", "adobe xd",
        "networking", "security", "penetration testing",
        "data visualization", "statistics", "etl",
        "responsive design", "accessibility", "webpack",
    ]

    text_lower = text.lower()
    found_skills = []
    for skill in skills_db:
        if skill in text_lower:
            found_skills.append(skill)
    result["skills"] = found_skills

    # --- EDUCATION ---
    education_keywords = [
        r"b\.?tech", r"b\.?sc", r"b\.?e\b", r"m\.?tech", r"m\.?sc", r"m\.?s\b",
        r"mba", r"ph\.?d", r"bachelor", r"master", r"diploma",
        r"b\.?a\b", r"m\.?a\b", r"associate",
        r"computer science", r"information technology",
        r"engineering", r"university", r"college", r"institute",
    ]
    edu_pattern = re.compile("|".join(education_keywords), re.IGNORECASE)
    for line in lines:
        if edu_pattern.search(line) and len(line) < 200:
            result["education"].append(line.strip())

    # Deduplicate education
    result["education"] = list(dict.fromkeys(result["education"]))[:5]

    # --- YEARS OF EXPERIENCE ---
    # Look for patterns like "5+ years", "3 years of experience", etc.
    yoe_pattern = r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of)?\s*(?:experience|exp)?'
    yoe_matches = re.findall(yoe_pattern, text, re.IGNORECASE)
    if yoe_matches:
        result["years_of_experience"] = max(int(y) for y in yoe_matches)
    else:
        # Estimate from date ranges (e.g., "2018 - 2023")
        date_ranges = re.findall(r'(20\d{2})\s*[-–—]\s*(20\d{2}|present|current)', text, re.IGNORECASE)
        if date_ranges:
            total_years = 0
            for start, end in date_ranges:
                start_year = int(start)
                end_year = 2025 if end.lower() in ["present", "current"] else int(end)
                total_years += max(end_year - start_year, 0)
            result["years_of_experience"] = min(total_years, 30)

    return result