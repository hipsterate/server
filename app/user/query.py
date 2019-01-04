from app.common.error import ExternalAPIFailError
from app.common.external import Facebook

from .model import User, UserSocial
from .error import (
    ValidatePasswordError, ValidateAccessTokenError, NotSupportedProviderError,
)
from .enum import SocialProvider


class UserQuery():
    def get_user(self, name, email):
        if name:
            user = User.query.filter_by(name=name).first()
        elif email:
            user = User.query.filter_by(email=email).first()
        else:
            raise ValueError('name or email are required')

        return user

    def get_user_by_provider(self, provider, social_id):
        if provider is SocialProvider.FACEBOOK:
            user = User.query.join(
                UserSocial, UserSocial.user_id == User.id,
            ).filter(
                UserSocial.social_id == social_id,
            ).first()
        else:
            raise NotSupportedProviderError(provider)

        return user

    def validate_password(self, name, email, password):
        user = self.get_user(name, email)
        if not user:
            raise ValueError('user not found')

        if user.password != password:
            raise ValidatePasswordError

        return user

    def validate_social_access_token(self, provider, id_, access_token):
        if provider is SocialProvider.FACEBOOK:
            try:
                Facebook.get_user(id_, access_token)
            except ExternalAPIFailError:
                raise ValidateAccessTokenError
        else:
            raise NotSupportedProviderError(provider)

        user = self.get_user_by_provider(provider, id_)
        if not user:
            raise ValueError('user not found')

        return user
