import unittest

import pytest

from app.user.command import UserCommand
from app.user.model import User, UserSocial

from test.test_app import DBTC


class TestUserCommand(DBTC):
    @pytest.fixture(scope='function', autouse=True)
    def setUp(self):
        self.command = UserCommand()

    def test_signup(self):
        name = 'my name'
        email = 'test@email.com'
        password = '1234'

        self.command.signup(name=name, email=email, password=password)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert user.email == email

    @unittest.mock.patch('app.common.external.Facebook.get_user')
    def test_social_signup(self, fb_get_user):
        name = 'my name'
        email = 'my@email.com'
        provider = 'facebook'
        id_ = '1234'
        access_token = 'abcd'

        fb_get_user.return_value = {
            'email': email,
            'name': name,
        }

        self.command.social_signup(
                provider=provider, id_=id_, access_token=access_token)

        user = User.query.filter_by(name=name).first()
        assert user is not None
        assert user.name == name
        assert user.email == email

        social = UserSocial.query.filter_by(user_id=user.id).first()
        assert social is not None
        assert social.social_provider == provider
        assert social.social_id == id_
