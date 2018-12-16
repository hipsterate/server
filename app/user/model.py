from datetime import datetime

from app.common.db import db, DateTimeUTC


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))
    name = db.Column(db.String(80), unique=True)
    lastfm_name = db.Column(db.String(80), unique=True)
    create_time = db.Column(
        DateTimeUTC, nullable=False, default=datetime.now())
    update_time = db.Column(
        DateTimeUTC, nullable=False, default=datetime.now(),
        onupdate=datetime.now())
