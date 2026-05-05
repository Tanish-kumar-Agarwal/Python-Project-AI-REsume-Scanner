"""
Learning Path Module (Feature 5)
Takes missing skills from Feature 2 and maps them to learning resources.
"""

from data.learning_db import get_resources


def build_learning_path(missing_skills):
    """
    Build a structured learning path from a list of missing skills.

    Returns dict with:
      - path: list of {skill, resources, total_hours}
      - total_hours: int
      - estimated_weeks: float (assuming 10 hrs/week)
      - skill_count: int
    """
    path = []
    grand_total_hours = 0

    for skill in missing_skills:
        resources = get_resources(skill)
        if resources:
            skill_hours = sum(r["hours"] for r in resources)
            grand_total_hours += skill_hours
            path.append({
                "skill": skill,
                "resources": resources,
                "total_hours": skill_hours,
            })
        else:
            # No resources found — still include the skill with a placeholder
            path.append({
                "skill": skill,
                "resources": [
                    {
                        "title": f"Search '{skill}' on Coursera or YouTube",
                        "platform": "Coursera",
                        "hours": 10,
                        "url": f"https://www.coursera.org/search?query={skill.replace(' ', '+')}",
                    }
                ],
                "total_hours": 10,
            })
            grand_total_hours += 10

    estimated_weeks = round(grand_total_hours / 10, 1) if grand_total_hours > 0 else 0

    return {
        "path": path,
        "total_hours": grand_total_hours,
        "estimated_weeks": estimated_weeks,
        "skill_count": len(path),
    }


def get_platform_badge(platform):
    """Return emoji + color for a platform badge."""
    badges = {
        "Coursera":  {"emoji": "🎓", "color": "#0056D2"},
        "YouTube":   {"emoji": "▶️",  "color": "#FF0000"},
        "Docs":      {"emoji": "📄", "color": "#4CAF50"},
        "Udemy":     {"emoji": "🎯", "color": "#A435F0"},
    }
    return badges.get(platform, {"emoji": "📚", "color": "#666666"})
