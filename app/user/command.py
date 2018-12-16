from flask_login import current_user, login_user

from app import db

from .model import User


class UserCommand():
    def signup(self, email, password):
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def signin(self, email):
        login_user(current_user)
