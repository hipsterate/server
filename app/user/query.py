import requests

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

    def validate_facebook_access_token(self, token):
        result = requests.get(
            f'https://graph.accountkit.com/v1.3/me/?access_token={token}')

        import pprint
        pprint.pprint(result.__dict__)

        if result.status_code != 200:
            return False

        return True
