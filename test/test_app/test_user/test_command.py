import pytest

from app.user.command import UserCommand
from app.user.model import User


class TestUserCommand():
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

    def test_signin(self, test_client):
        """ API test for request context """

        email = 'test@email.com'
        password = '1234'

        result = test_client.post('user/signin', data={
            'email': email,
            'password': password,
        })

        assert result.headers.get('Set-Cookie') is not None
        assert 'session' in result.headers['Set-Cookie']
