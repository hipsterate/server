from app.user.command import UserCommand

from test.test_app import DBTC


class TestUserAPI(DBTC):
    def test_signin(self, test_client):
        email = 'test@email.com'
        password = '1234'

        command = UserCommand()
        command.signup(email=email, password=password)

        result = test_client.post('user/signin', data={
            'email': email,
            'password': password,
        })

        assert result.headers.get('Set-Cookie') is not None
        assert 'session' in result.headers['Set-Cookie']
