from trial import db, create_app
from trial.models import Announcement
import datetime

app = create_app()
with app.app_context():
    # Check if any announcements exist
    if not Announcement.query.first():
        a1 = Announcement(
            title="Road Maintenance", 
            content="Scheduled maintenance on highway N1 starting next week.",
            date_posted=datetime.datetime.utcnow(),
            is_active=True
        )
        a2 = Announcement(
            title="Tender Notice", 
            content="New tenders available for bridge construction.",
            date_posted=datetime.datetime.utcnow(),
            is_active=True
        )
        db.session.add(a1)
        db.session.add(a2)
        db.session.commit()
        print("Announcements seeded successfully.")
    else:
        print("Announcements already exist.")
