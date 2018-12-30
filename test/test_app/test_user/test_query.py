import pytest
import requests

from app.common.error import ExternalAPIFailError
from app.user.command import UserCommand
from app.user.query import UserQuery
from app.user.error import ValidatePasswordError, ValidateAccessTokenError

from test.test_app import DBTC


class TestUserQueryValidatePassword(DBTC):
    @pytest.fixture(scope='function', autouse=True)
    def setUp(self, tx):
        self.query = UserQuery()

        self.name = 'your name'
        self.email = 'your@email.com'
        self.password = 'password'

        command = UserCommand()
        command.signup(self.name, self.email, self.password)

    def test_success(self):
        query_user = self.query.validate_password(
                self.name, self.email, self.password)

        assert query_user is not None
        assert query_user.name == self.name
        assert query_user.email == self.email

    def test_wrong_password_raise_validate_error(self):
        wrong_password = 'wrong_password'

        with pytest.raises(ValidatePasswordError):
            self.query.validate_password(self.name, self.email, wrong_password)


class TestUserQueryValidateSocialAccessToken(DBTC):
    @pytest.fixture(scope='function', autouse=True)
    def setUp(self, tx, mocker):
        self.email = 'your@email.com'
        self.name = 'yourname'

        fb_get_user = mocker.patch('app.common.external.Facebook.get_user')
        fb_get_user.return_value = {
            'email': self.email,
            'name': self.name,
        }

        self.query = UserQuery()

        self.provider = 'facebook'
        self.id = 'social_id'
        self.access_token = 'social_access_token'

        command = UserCommand()
        command.social_signup(self.provider, self.id, self.access_token)

    def test_success(self):
        query_user = self.query.validate_social_access_token(
                self.provider, self.id, self.access_token)

        assert query_user is not None
        assert query_user.name == self.name
        assert query_user.email == self.email

    def test_fail_external_raise_validate_error(self, mocker):
        fb_get_user = mocker.patch('app.common.external.Facebook.get_user')
        response = requests.Response()
        response.status_code = 403
        fb_get_user.side_effect = ExternalAPIFailError(self.provider, response)

        with pytest.raises(ValidateAccessTokenError):
            self.query.validate_social_access_token(
                    self.provider, self.id, self.access_token)
