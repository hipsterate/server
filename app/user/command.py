from app.common.command import Command
from app.common.external import Facebook

from .model import User, UserSocial
from .error import NotSupportedProviderError


class UserCommand(Command):
    def signup(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        self.insert(new_user)

    def social_signup(self, provider, id_, access_token):
        if provider == 'facebook':
            fetched = Facebook.get_user(id_, access_token)
        else:
            raise NotSupportedProviderError(provider)

        new_user = User(email=fetched['email'], name=fetched['name'])
        self.insert(new_user)
        new_social = UserSocial(
                user=new_user, social_provider=provider, social_id=id_)
        self.insert(new_social)
