from app.common.command import Command
from app.common.external import Facebook, LastFM

from .model import User, UserSocial
from .error import NotSupportedProviderError
from .enum import SocialProvider


class UserCommand(Command):
    def signup(self, name, email, password):
        if not name or not password:
            raise ValueError('name, password are required')

        new_user = User(name=name, email=email, password=password)
        self.insert(new_user)

    def social_signup(self, provider, id_, access_token):
        if provider is SocialProvider.FACEBOOK:
            fetched = Facebook.get_user(id_, access_token)
        else:
            raise NotSupportedProviderError(provider)

        new_user = User(email=fetched['email'], name=fetched['name'])
        self.insert(new_user)
        new_social = UserSocial(
                user=new_user, social_provider=provider, social_id=id_)
        self.insert(new_social)

    def connect_lastfm(self, user_id, token):
        session_key, lastfm_name = LastFM.get_session(token)
        User.query.update_lastfm_name(user_id, lastfm_name)
