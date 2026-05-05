"""
STAR Question Generator (Feature 6)
Filters questions from star_bank by user's detected role and skills.
"""

from data.star_bank import get_questions_for_role, STAR_BANK


def get_star_questions(role, skills=None, limit=8):
    """
    Get filtered STAR questions for a role + skills.
    Wrapper around star_bank.get_questions_for_role().
    """
    return get_questions_for_role(role, skills, limit)


def get_all_roles():
    """Return all unique role tags from the STAR bank."""
    roles = set()
    for q in STAR_BANK:
        for tag in q["role_tags"]:
            roles.add(tag)
    return sorted(roles)


def get_all_skill_tags():
    """Return all unique skill tags from the STAR bank."""
    skills = set()
    for q in STAR_BANK:
        for tag in q["skill_tags"]:
            skills.add(tag)
    return sorted(skills)
