from flask_login import UserMixin

from app.common.db import db, DateTimeUTC
from app.common.util import utcnow


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))
    name = db.Column(db.String(80), unique=True)
    lastfm_name = db.Column(db.String(80), unique=True)
    create_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow)
    update_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow, onupdate=utcnow)


class UserSocial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    social_provider = db.Column(db.String(80), unique=True)
    social_id = db.Column(db.String(80), unique=True)
    create_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow)
    update_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow, onupdate=utcnow)

    user = db.relationship('User')
