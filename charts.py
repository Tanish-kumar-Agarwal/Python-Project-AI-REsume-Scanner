"""
Charts module — matplotlib charts for the dashboard.
Covers: skill chart, skill gap chart, career roadmap timeline, ATS score breakdown.
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Use non-interactive backend for Streamlit
matplotlib.use("Agg")

# Consistent color palette
COLORS = {
    "primary": "#667eea",
    "secondary": "#764ba2",
    "success": "#4CAF50",
    "danger": "#f5576c",
    "warning": "#FFC107",
    "info": "#4facfe",
    "light_bg": "#f8f9fa",
    "accent1": "#f093fb",
    "accent2": "#43e97b",
    "accent3": "#38f9d7",
    "gray": "#e0e0e0",
}


def skill_chart(user_skills, required_skills):
    """
    Create a bar chart showing user skills vs required skills.
    """
    values = []
    labels = []

    for skill in required_skills:
        labels.append(skill.title())
        values.append(1 if skill in user_skills else 0)

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = [COLORS["primary"] if v == 1 else COLORS["gray"] for v in values]
    ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_ylabel('Skill Level', fontsize=12, fontweight='bold')
    ax.set_title('Your Skills Assessment', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 1.2)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    return fig


def skill_gap_chart(user_skills, required_skills):
    """
    Create a horizontal bar chart showing skill gaps.
    Green = have, Red = missing.
    """
    fig, ax = plt.subplots(figsize=(10, max(6, len(required_skills) * 0.5)))

    labels = [s.title() for s in required_skills]
    user_has = [1 if s.lower() in [u.lower() for u in user_skills] else 0 for s in required_skills]

    colors = [COLORS["success"] if v == 1 else COLORS["danger"] for v in user_has]
    status_labels = ["✓ Have" if v == 1 else "✗ Need" for v in user_has]

    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, [1] * len(labels), color=colors, alpha=0.8, height=0.6)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlim(0, 1.3)
    ax.set_xticks([])
    ax.set_title("Skill Gap Analysis", fontsize=14, fontweight="bold", pad=15)

    # Add status labels on bars
    for i, (bar, label) in enumerate(zip(bars, status_labels)):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height() / 2,
                label, va="center", fontsize=9, fontweight="bold")

    ax.invert_yaxis()
    plt.tight_layout()
    return fig


def career_roadmap_chart(milestones):
    """
    Create a horizontal timeline chart for career progression.
    milestones: list of dicts with 'title' and 'years'.
    """
    if not milestones:
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.text(0.5, 0.5, "No roadmap data available", ha="center", va="center", fontsize=14)
        ax.axis("off")
        return fig

    fig, ax = plt.subplots(figsize=(14, 4))

    n = len(milestones)
    x_positions = np.linspace(0.1, 0.9, n)
    y = 0.5

    # Draw connecting line
    ax.plot([x_positions[0], x_positions[-1]], [y, y],
            color=COLORS["primary"], linewidth=3, zorder=1)

    # Draw milestone circles and labels
    gradient_colors = [COLORS["primary"], COLORS["secondary"], COLORS["accent1"],
                       COLORS["danger"], COLORS["accent2"]]

    for i, (x, ms) in enumerate(zip(x_positions, milestones)):
        color = gradient_colors[i % len(gradient_colors)]

        # Circle
        ax.scatter(x, y, s=200, color=color, zorder=3, edgecolors="white", linewidth=2)

        # Title above
        ax.text(x, y + 0.15, ms["title"], ha="center", va="bottom",
                fontsize=8, fontweight="bold", wrap=True,
                bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.15))

        # Years below
        ax.text(x, y - 0.12, f"{ms['years']} yrs", ha="center", va="top",
                fontsize=8, color="#666")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Career Progression Timeline", fontsize=14, fontweight="bold", pad=20)

    plt.tight_layout()
    return fig


def ats_score_chart(breakdown):
    """
    Create a horizontal bar chart for ATS score breakdown.
    breakdown: dict of {category: {score, max, detail}}.
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    categories = list(breakdown.keys())
    scores = [breakdown[c]["score"] for c in categories]
    maxes = [breakdown[c]["max"] for c in categories]
    percentages = [s / m * 100 if m > 0 else 0 for s, m in zip(scores, maxes)]

    y_pos = np.arange(len(categories))

    # Background bars (max)
    ax.barh(y_pos, [100] * len(categories), color=COLORS["gray"], alpha=0.3, height=0.5)

    # Score bars with gradient colors
    bar_colors = []
    for pct in percentages:
        if pct >= 80:
            bar_colors.append(COLORS["success"])
        elif pct >= 60:
            bar_colors.append(COLORS["warning"])
        else:
            bar_colors.append(COLORS["danger"])

    bars = ax.barh(y_pos, percentages, color=bar_colors, alpha=0.85, height=0.5)

    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=10)
    ax.set_xlim(0, 110)
    ax.set_xlabel("Score (%)", fontsize=11)
    ax.set_title("ATS Score Breakdown", fontsize=14, fontweight="bold", pad=15)

    # Add score text on bars
    for i, (bar, score, mx) in enumerate(zip(bars, scores, maxes)):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
                f"{score}/{mx}", va="center", fontsize=9, fontweight="bold")

    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.2)
    plt.tight_layout()
    return fig


def learning_timeline_chart(path_data):
    """
    Create a visual timeline of learning path with hours per skill.
    path_data: list of {skill, total_hours}.
    """
    if not path_data:
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.text(0.5, 0.5, "No learning path data", ha="center", va="center", fontsize=14)
        ax.axis("off")
        return fig

    fig, ax = plt.subplots(figsize=(10, max(4, len(path_data) * 0.6)))

    skills = [p["skill"].title() for p in path_data]
    hours = [p["total_hours"] for p in path_data]

    y_pos = np.arange(len(skills))

    # Gradient from primary to accent
    colors_list = []
    for i in range(len(skills)):
        ratio = i / max(len(skills) - 1, 1)
        r = int(102 + (67 - 102) * ratio)
        g = int(126 + (229 - 126) * ratio)
        b = int(234 + (209 - 234) * ratio)
        colors_list.append(f"#{r:02x}{g:02x}{b:02x}")

    bars = ax.barh(y_pos, hours, color=colors_list, alpha=0.85, height=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(skills, fontsize=10)
    ax.set_xlabel("Estimated Hours", fontsize=11)
    ax.set_title("Learning Path Timeline", fontsize=14, fontweight="bold", pad=15)

    # Add hours text
    for bar, h in zip(bars, hours):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                f"{h}h", va="center", fontsize=9, fontweight="bold")

    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.2)
    plt.tight_layout()
    return fig