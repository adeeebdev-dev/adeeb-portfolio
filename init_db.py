"""
One-time initialization script.
Run this once to create database tables and the first admin user.

Usage:
    python init_db.py
"""

import os
from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database tables created.")

    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_password = os.environ.get('ADMIN_PASSWORD')

    if not admin_password:
        print("⚠️  ADMIN_PASSWORD not set in .env — skipping admin creation.")
    else:
        existing = User.query.filter_by(username=admin_username).first()
        if existing:
            print(f"ℹ️  Admin user '{admin_username}' already exists — skipping.")
        else:
            admin = User(username=admin_username)
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f"✅ Admin user '{admin_username}' created successfully.")