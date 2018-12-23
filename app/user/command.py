from flask_login import login_user

from app.common.command import Command

from .model import User


class UserCommand(Command):
    def signup(self, email, password):
        new_user = User(email=email, password=password)
        self.insert(new_user)

    def signin(self, user):
        login_user(user)
