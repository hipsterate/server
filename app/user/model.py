from flask_sqlalchemy import BaseQuery
from flask_login import UserMixin

from app.common.db import db, DateTimeUTC
from app.common.util import utcnow

from .enum import SocialProvider


class UserQuery(BaseQuery):
    def update_lastfm_name(self, user_id, lastfm_name):
        return self.filter(
            User.id == user_id,
        ).update({
            'lastfm_name': lastfm_name,
        })


class User(db.Model, UserMixin):
    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
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
    provider = db.Column(db.Enum(SocialProvider), nullable=False)
    social_id = db.Column(db.String(80), unique=True, nullable=False)
    create_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow)
    update_time = db.Column(
        DateTimeUTC, nullable=False, default=utcnow, onupdate=utcnow)

    user = db.relationship('User')
