import pytest

from app.user.command import UserCommand
from app.user.model import User

from test.test_app import DBTC


class TestUserCommand(DBTC):
    @pytest.fixture(scope='function', autouse=True)
    def setUp(self):
        self.command = UserCommand()

    def test_signup(self):
        email = 'test@email.com'
        password = '1234'

        self.command.signup(email=email, password=password)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert user.email == email
