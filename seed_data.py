"""
Seeds initial portfolio data — run once after init_db.py.
Safe to re-run: skips records that already exist (by slug/title).

Usage:
    python seed_data.py
"""

from datetime import date
from app import create_app
from extensions import db
from models import Project, Skill, Experience, Certificate

app = create_app()

PROJECTS = [
    dict(title="Website Analytics Demo", slug="website-analytics-demo",
         short_description="A Flask-based analytics dashboard demonstrating data tracking and visualization concepts.",
         full_description="A demo application built to explore how basic website analytics can be tracked and visualized using Flask and SQLite.",
         category="Python", technologies="Python, Flask, HTML, CSS, JavaScript, SQLite",
         features="Tracks page visits\nDisplays basic visualization charts\nSQLite-backed data storage",
         github_url="https://github.com/adeeebdev-dev/website_analytics_demo",
         live_demo_url="https://yourwebsite.pythonanywhere.com",
         is_featured=True, order_index=1),

    dict(title="Restaurant Management System", slug="restaurant-management-system",
         short_description="A Flask + SQLite system for managing restaurant orders, menus, and daily operations.",
         full_description="A practical academic project built to simulate order handling and menu management for a restaurant using Flask and SQLite.",
         category="Python", technologies="Python, Flask, HTML, CSS, JavaScript, SQLite",
         features="Menu and order management\nBasic admin controls\nSQLite database backend",
         is_featured=True, order_index=2),

    dict(title="Voting Management System", slug="voting-management-system",
         short_description="A web-based voting system built with JavaScript and SQL for handling votes and results.",
         full_description="An academic project simulating a voting process, covering form handling, data storage, and result display.",
         category="JavaScript", technologies="JavaScript, HTML, CSS, SQL/MySQL",
         features="Voter interface\nResult tabulation\nBasic data validation",
         order_index=3),

    dict(title="Learning Management System", slug="learning-management-system",
         short_description="A Java-based system applying OOP principles to manage courses and learning content.",
         full_description="An academic project focused on applying object-oriented programming concepts to a learning management use case.",
         category="Java", technologies="Java, OOP",
         features="Course structure modeling\nObject-oriented design\nCore CRUD operations",
         order_index=4),

    dict(title="Sadar Marble Store", slug="sadar-marble-store",
         short_description="A business-style website built for a marble store, focused on showcasing products and services.",
         full_description="A front-end focused website built to represent a local marble store's products and contact information.",
         category="Web Development", technologies="HTML, CSS, JavaScript, Flask",
         features="Product showcase layout\nResponsive design\nContact section",
         order_index=5),

    dict(title="AI Interview Preparation System", slug="ai-interview-preparation-system",
         short_description="A Flask application to help users practice interview questions with structured feedback.",
         full_description="An application exploring how AI concepts can be applied to help users prepare for interviews through structured practice sessions.",
         category="AI", technologies="Python, Flask, HTML, CSS, JavaScript, SQL/MySQL",
         features="Structured question practice\nFeedback-oriented flow\nDatabase-backed question storage",
         is_featured=True, order_index=6),

    dict(title="Birthday / Memorial Website", slug="birthday-memorial-website",
         short_description="A personal web project created as a respectful tribute page.",
         full_description="A personal, non-commercial web project designed with a respectful and simple layout.",
         category="Web Development", technologies="HTML, CSS, JavaScript",
         features="Simple respectful layout\nPersonal content sections",
         order_index=7),

    dict(title="Computer Networking Projects", slug="computer-networking-projects",
         short_description="Academic projects exploring practical computer networking concepts.",
         full_description="A collection of academic exercises covering practical networking concepts as part of university coursework.",
         category="Academic", technologies="Networking Fundamentals",
         features="Academic networking exercises\nPractical concept application",
         order_index=8),

    dict(title="n8n Automation Projects", slug="n8n-automation-projects",
         short_description="A set of workflow automation projects built using n8n, including bots and integrations.",
         full_description="Practical automation workflows including a clinic appointment system, a Telegram booking bot, and Gmail + Google Sheets integrations.",
         category="Automation", technologies="n8n, Telegram API, Gmail API, Google Sheets",
         features="Clinic Appointment Automation\nTelegram Appointment Booking Bot\nGoogle Sheets + Gmail Automation",
         is_featured=True, order_index=9),
]

SKILLS = [
    ("Programming", ["Python", "Java", "JavaScript", "C++"]),
    ("Web Development", ["HTML", "CSS", "JavaScript", "Flask"]),
    ("Database", ["SQL", "MySQL", "SQLite"]),
    ("Concepts", ["Object-Oriented Programming", "Data Structures", "REST/API Fundamentals"]),
    ("Automation", ["n8n", "Workflow Automation", "Telegram Automation", "Gmail Automation", "Google Sheets Automation"]),
    ("AI", ["Generative AI", "AI Application Concepts"]),
]

EXPERIENCE = dict(
    organization="Ministry of Finance, Government of Pakistan",
    role="IT Intern",
    location="Finance Division, IT Wing, Islamabad",
    start_date=date(2026, 7, 27),
    end_date=date(2026, 8, 16),
    is_current=False,
    description="Working in the IT Wing on practical software and technology-related tasks, gaining exposure to real-world government IT workflows.",
    order_index=1
)

CERTIFICATE = dict(
    title="Generative AI for Beginners",
    organization="Simplilearn SkillUp",
    issue_date=date(2026, 6, 1),
    certificate_code="10356806",
    order_index=1
)

with app.app_context():
    for p in PROJECTS:
        if not Project.query.filter_by(slug=p['slug']).first():
            db.session.add(Project(**p))
    print("✅ Projects seeded.")

    for category, names in SKILLS:
        for i, name in enumerate(names):
            if not Skill.query.filter_by(category=category, name=name).first():
                db.session.add(Skill(category=category, name=name, order_index=i))
    print("✅ Skills seeded.")

    if not Experience.query.filter_by(organization=EXPERIENCE['organization']).first():
        db.session.add(Experience(**EXPERIENCE))
    print("✅ Experience seeded.")

    if not Certificate.query.filter_by(certificate_code=CERTIFICATE['certificate_code']).first():
        db.session.add(Certificate(**CERTIFICATE))
    print("✅ Certificate seeded.")

    db.session.commit()
    print("🎉 Seeding complete.")