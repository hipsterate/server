from flask_login import login_user

from app import db

from .model import User


class UserCommand():
    def signup(self, email, password):
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def signin(self, user):
        login_user(user)
