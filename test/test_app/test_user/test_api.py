class TestUserAPI():
    def test_signin(self, test_client):
        email = 'test@email.com'
        password = '1234'

        result = test_client.post('user/signin', data={
            'email': email,
            'password': password,
        })

        assert result.headers.get('Set-Cookie') is not None
        assert 'session' in result.headers['Set-Cookie']
