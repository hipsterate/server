from datetime import datetime

from app.common.db import db, DateTimeUTC


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lastfm_name = db.Column(db.String(80), unique=True)
    create_time = db.Column(
        DateTimeUTC, nullable=False, default=datetime.now())
    update_time = db.Column(
        DateTimeUTC, nullable=False, default=datetime.now(),
        onupdate=datetime.now())
