from app import db
from app.user.model import User


class UserCommand():
    def signup(self, name, email, social=None):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

    def signin(self):
        pass
