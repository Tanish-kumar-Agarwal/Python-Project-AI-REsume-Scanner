"""
Resume Maker (Feature 4)
Generates a clean, professional PDF resume matching Jake's LaTeX template style.
Uses fpdf2 for PDF generation.

Style: Single-column, tight margins, 10.5pt, bold section headers, horizontal rules.
"""

from fpdf import FPDF
import io


class ResumePDF(FPDF):
    """Custom PDF class for Jake-style resume generation."""

    def __init__(self):
        super().__init__(format="letter")
        self.set_auto_page_break(auto=True, margin=15)
        # Tight margins like Jake's template
        self.set_margins(left=12, top=12, right=12)

    def header(self):
        pass  # No header — name is part of content

    def footer(self):
        pass  # No footer for clean resume look

    def add_name_header(self, name, email="", phone="", linkedin="", github="", location=""):
        """Bold centered name + contact info line."""
        # Name
        self.set_font("Helvetica", "B", 18)
        self.cell(0, 8, name.strip(), new_x="LMARGIN", new_y="NEXT", align="C")

        # Contact line
        contact_parts = []
        if phone:
            contact_parts.append(phone.strip())
        if email:
            contact_parts.append(email.strip())
        if linkedin:
            contact_parts.append(linkedin.strip())
        if github:
            contact_parts.append(github.strip())
        if location:
            contact_parts.append(location.strip())

        if contact_parts:
            self.set_font("Helvetica", "", 9)
            contact_line = "  |  ".join(contact_parts)
            self.cell(0, 5, contact_line, new_x="LMARGIN", new_y="NEXT", align="C")

        self.ln(2)

    def add_section_header(self, title):
        """Bold section header with horizontal rule underneath."""
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
        # Horizontal rule
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.5)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(3)

    def add_experience_entry(self, title, company, location, dates, bullets):
        """Add a work experience entry."""
        # Title + Company on one line
        self.set_font("Helvetica", "B", 10)
        title_company = f"{title.strip()}"
        if company:
            title_company += f"  —  {company.strip()}"

        self.set_font("Helvetica", "B", 10)
        # Title + company left, dates right
        self.cell(0, 5, title_company, new_x="LMARGIN", new_y="NEXT")

        # Location + Dates line
        loc_date_parts = []
        if location:
            loc_date_parts.append(location.strip())
        if dates:
            loc_date_parts.append(dates.strip())
        if loc_date_parts:
            self.set_font("Helvetica", "I", 9)
            self.cell(0, 4, "  |  ".join(loc_date_parts), new_x="LMARGIN", new_y="NEXT")

        # Bullet points
        self.set_font("Helvetica", "", 9.5)
        for bullet in bullets:
            bullet = bullet.strip()
            if bullet:
                self.cell(5)  # indent
                self.cell(3, 4, chr(8226))  # bullet character
                self.cell(2)
                # Multi-line support
                self.multi_cell(0, 4, f" {bullet}", new_x="LMARGIN")

        self.ln(2)

    def add_education_entry(self, degree, school, location, dates, details=""):
        """Add an education entry."""
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 5, f"{degree.strip()}", new_x="LMARGIN", new_y="NEXT")

        line2_parts = []
        if school:
            line2_parts.append(school.strip())
        if location:
            line2_parts.append(location.strip())
        if dates:
            line2_parts.append(dates.strip())

        if line2_parts:
            self.set_font("Helvetica", "I", 9)
            self.cell(0, 4, "  |  ".join(line2_parts), new_x="LMARGIN", new_y="NEXT")

        if details:
            self.set_font("Helvetica", "", 9.5)
            self.cell(5)
            self.multi_cell(0, 4, details.strip(), new_x="LMARGIN")

        self.ln(2)

    def add_skills_section(self, skills_text):
        """Add skills as a wrapped paragraph."""
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 4.5, skills_text.strip())
        self.ln(2)

    def add_summary(self, summary_text):
        """Add a professional summary paragraph."""
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 4.5, summary_text.strip())
        self.ln(2)


def generate_resume_pdf(data):
    """
    Generate a PDF resume from form data.

    Args:
        data: dict with keys:
            - name (str)
            - email (str)
            - phone (str)
            - linkedin (str, optional)
            - github (str, optional)
            - location (str, optional)
            - summary (str)
            - experiences: list of dicts {title, company, location, dates, bullets: [str]}
            - education: list of dicts {degree, school, location, dates, details}
            - skills (str)

    Returns:
        bytes: PDF file content
    """
    pdf = ResumePDF()
    pdf.add_page()

    # Header
    pdf.add_name_header(
        name=data.get("name", ""),
        email=data.get("email", ""),
        phone=data.get("phone", ""),
        linkedin=data.get("linkedin", ""),
        github=data.get("github", ""),
        location=data.get("location", ""),
    )

    # Summary
    summary = data.get("summary", "").strip()
    if summary:
        pdf.add_section_header("Professional Summary")
        pdf.add_summary(summary)

    # Experience
    experiences = data.get("experiences", [])
    if experiences:
        pdf.add_section_header("Experience")
        for exp in experiences:
            pdf.add_experience_entry(
                title=exp.get("title", ""),
                company=exp.get("company", ""),
                location=exp.get("location", ""),
                dates=exp.get("dates", ""),
                bullets=exp.get("bullets", []),
            )

    # Education
    education = data.get("education", [])
    if education:
        pdf.add_section_header("Education")
        for edu in education:
            pdf.add_education_entry(
                degree=edu.get("degree", ""),
                school=edu.get("school", ""),
                location=edu.get("location", ""),
                dates=edu.get("dates", ""),
                details=edu.get("details", ""),
            )

    # Skills
    skills = data.get("skills", "").strip()
    if skills:
        pdf.add_section_header("Technical Skills")
        pdf.add_skills_section(skills)

    # Output as bytes
    return pdf.output()
