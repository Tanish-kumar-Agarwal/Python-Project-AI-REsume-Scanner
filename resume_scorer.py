"""
ATS Resume Scoring Engine (Feature 7)
Pure rule-based scoring out of 100.

Breakdown:
  - Keyword hit rate vs target role skills → 30 pts
  - Section presence (summary, experience, education, skills) → 20 pts
  - Length (400–700 words ideal) → 15 pts
  - Action verb usage → 15 pts
  - Format cleanliness (no tables/images/columns detected) → 20 pts
"""

import re
from data.skills_db import get_required_skills


# Common action verbs that ATS systems look for
ACTION_VERBS = [
    "managed", "led", "built", "reduced", "increased", "developed",
    "designed", "implemented", "created", "improved", "launched",
    "achieved", "delivered", "optimized", "automated", "analyzed",
    "coordinated", "executed", "established", "generated", "maintained",
    "negotiated", "organized", "produced", "resolved", "streamlined",
    "supervised", "trained", "transformed", "spearheaded", "pioneered",
    "collaborated", "facilitated", "mentored", "orchestrated", "revamped",
]

# Section headers to look for
REQUIRED_SECTIONS = {
    "summary":    ["summary", "objective", "profile", "about me", "professional summary"],
    "experience": ["experience", "work experience", "employment", "work history", "professional experience"],
    "education":  ["education", "academic", "qualification", "certifications", "degree"],
    "skills":     ["skills", "technical skills", "core competencies", "proficiencies", "technologies"],
}

# Format red flags
FORMAT_RED_FLAGS = [
    r"\|.*\|.*\|",          # table-like patterns (pipes)
    r"<img",                # embedded images
    r"<table",              # HTML tables
    r"\t{3,}",              # excessive tabs (column layouts)
    r"[█▓▒░■□●○◆◇]",       # graphic characters
]


def score_keywords(text, target_role):
    """
    Score keyword hit rate vs target role skills → max 30 pts.
    """
    text_lower = text.lower()
    required = get_required_skills(target_role)

    if not required:
        return 0, [], [], "No skills data available for this role."

    found = [s for s in required if s.lower() in text_lower]
    missing = [s for s in required if s.lower() not in text_lower]

    hit_rate = len(found) / len(required) if required else 0
    score = round(hit_rate * 30)

    detail = f"{len(found)}/{len(required)} keywords matched ({hit_rate:.0%})"
    return score, found, missing, detail


def score_sections(text):
    """
    Score section presence → max 20 pts (5 per section).
    """
    text_lower = text.lower()
    found_sections = []
    missing_sections = []

    for section_name, keywords in REQUIRED_SECTIONS.items():
        if any(kw in text_lower for kw in keywords):
            found_sections.append(section_name)
        else:
            missing_sections.append(section_name)

    score = len(found_sections) * 5  # 5 pts each, max 20
    detail = f"{len(found_sections)}/4 sections found"
    return score, found_sections, missing_sections, detail


def score_length(text):
    """
    Score document length → max 15 pts.
    Ideal: 400–700 words.
    """
    word_count = len(text.split())

    if 400 <= word_count <= 700:
        score = 15
        detail = f"{word_count} words — ideal length ✓"
    elif 300 <= word_count < 400:
        score = 10
        detail = f"{word_count} words — slightly short, aim for 400+"
    elif 700 < word_count <= 900:
        score = 10
        detail = f"{word_count} words — slightly long, trim to ~700"
    elif 200 <= word_count < 300:
        score = 5
        detail = f"{word_count} words — too short, add more detail"
    elif 900 < word_count <= 1200:
        score = 5
        detail = f"{word_count} words — too long, condense content"
    else:
        score = 2
        detail = f"{word_count} words — significantly outside ideal range (400–700)"

    return score, word_count, detail


def score_action_verbs(text):
    """
    Score action verb usage → max 15 pts.
    """
    text_lower = text.lower()
    found_verbs = [v for v in ACTION_VERBS if v in text_lower]
    unique_count = len(set(found_verbs))

    if unique_count >= 10:
        score = 15
    elif unique_count >= 7:
        score = 12
    elif unique_count >= 4:
        score = 8
    elif unique_count >= 2:
        score = 5
    else:
        score = 2

    detail = f"{unique_count} action verbs found"
    return score, found_verbs, detail


def score_format(text):
    """
    Score format cleanliness → max 20 pts.
    Deduct points for each red flag pattern detected.
    """
    issues = []
    deductions = 0

    for pattern in FORMAT_RED_FLAGS:
        matches = re.findall(pattern, text)
        if matches:
            issues.append(f"Detected format issue: pattern '{pattern}' found {len(matches)} time(s)")
            deductions += 5

    score = max(20 - deductions, 0)

    if not issues:
        detail = "Clean format — no tables, images, or complex layouts detected ✓"
    else:
        detail = f"{len(issues)} format issue(s) detected"

    return score, issues, detail


def calculate_ats_score(text, target_role="software engineer"):
    """
    Calculate full ATS score with breakdown.

    Returns dict with:
      - total_score (int, 0-100)
      - breakdown (dict of category scores)
      - fixes (list of actionable improvement suggestions)
      - grade (str: A/B/C/D/F)
    """
    # Calculate each component
    kw_score, kw_found, kw_missing, kw_detail = score_keywords(text, target_role)
    sec_score, sec_found, sec_missing, sec_detail = score_sections(text)
    len_score, word_count, len_detail = score_length(text)
    verb_score, verbs_found, verb_detail = score_action_verbs(text)
    fmt_score, fmt_issues, fmt_detail = score_format(text)

    total_score = kw_score + sec_score + len_score + verb_score + fmt_score

    # Build breakdown
    breakdown = {
        "Keyword Match (30)": {"score": kw_score, "max": 30, "detail": kw_detail},
        "Section Presence (20)": {"score": sec_score, "max": 20, "detail": sec_detail},
        "Document Length (15)": {"score": len_score, "max": 15, "detail": len_detail},
        "Action Verbs (15)": {"score": verb_score, "max": 15, "detail": verb_detail},
        "Format Cleanliness (20)": {"score": fmt_score, "max": 20, "detail": fmt_detail},
    }

    # Build fix suggestions
    fixes = []
    if kw_missing:
        fixes.append(f"🔑 Add missing keywords: {', '.join(kw_missing[:5])}")
    if sec_missing:
        fixes.append(f"📋 Add missing sections: {', '.join(sec_missing)}")
    if word_count < 400:
        fixes.append(f"📏 Resume is too short ({word_count} words). Expand to 400–700 words.")
    elif word_count > 700:
        fixes.append(f"📏 Resume is too long ({word_count} words). Trim to 400–700 words.")
    if len(verbs_found) < 4:
        fixes.append(f"💪 Use more action verbs (managed, led, built, reduced, etc.)")
    if fmt_issues:
        fixes.append("🧹 Remove tables, images, or complex column layouts for better ATS parsing.")

    if not fixes:
        fixes.append("✅ Great job! Your resume is well-optimized for ATS systems.")

    # Grade
    if total_score >= 85:
        grade = "A"
    elif total_score >= 70:
        grade = "B"
    elif total_score >= 55:
        grade = "C"
    elif total_score >= 40:
        grade = "D"
    else:
        grade = "F"

    return {
        "total_score": total_score,
        "grade": grade,
        "breakdown": breakdown,
        "fixes": fixes,
        "keywords_found": kw_found,
        "keywords_missing": kw_missing,
        "sections_found": sec_found,
        "sections_missing": sec_missing,
        "word_count": word_count,
        "action_verbs": verbs_found,
        "format_issues": fmt_issues,
    }
