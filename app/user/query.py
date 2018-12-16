from .model import User


class UserQuery():
    def get_user(self, email=None):
        if email:
            return User.query.filter_by(email=email).first()

    def validate_password(self, email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return False

        if user.password != password:
            return False

        return True
