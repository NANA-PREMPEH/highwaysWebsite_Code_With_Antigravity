from trial import db, create_app
from trial.models import Announcement

app = create_app()
with app.app_context():
    announcements = Announcement.query.all()
    print(f"Total announcements: {len(announcements)}")
    for a in announcements:
        print(f"ID: {a.id}, Title: {a.title}, Active: {a.is_active}")
